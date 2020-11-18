from django.contrib.auth.models import User

import graphene
from graphene.relay import Node
from graphql_relay import from_global_id
from graphene_django import DjangoObjectType, DjangoListField
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_jwt.decorators import login_required
from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation


from backend.application.models import Application, ApplicationImage, \
    Option, Order, Product, Weight, Amount
from backend.application.forms import ApplicationForm, ProductForm
from backend.registration.schema import UserType
from backend.registration.decorators import check_application_permission_by_slug


# Types
# =========

class ApplicationImageType(DjangoObjectType):
    class Meta:
        model = ApplicationImage
        fields = '__all__'


class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application
        fields = '__all__'

    def resolve_members(self, info):
        members = User.objects.filter(member_application=self)
        if info.context.user.is_authenticated:
            return members
        else:
            return members.only('id')

    def resolve_admins(self, info):
        if info.context.user.is_authenticated:
            return User.objects.filter(admin_application=self)
        else:
            return User.objects.filter(admin_application=self).only('id')


class OptionType(DjangoObjectType):
    class Meta:
        model = Option
        fields = '__all__'
        interfaces = (Node, )
        filter_fields = ['id', 'application__name', 'application__slug']


class AmountType(DjangoObjectType):
    class Meta:
        model = Amount
        fields = '__all__'


class OrderType(DjangoObjectType):
    class Meta:
        interfaces = (Node, )
        model = Order
        fields = '__all__'
        filter_fields = ['id', 'application__name',
                         'user',  'application__slug']


class ProductType(DjangoObjectType):
    class Meta:
        interfaces = (Node, )
        model = Product
        fields = '__all__'
        filter_fields = [
            'id', 'application__slug', 'application__name', 'display']


class WeightType(DjangoObjectType):
    class Meta:
        interfaces = (Node, )
        model = Weight
        fields = '__all__'
        filter_fields = ['id', 'application__name',  'application__slug']


# Mutations
# ==========

class AddProduct(DjangoModelFormMutation):

    product = graphene.Field(ProductType)
    login_required = True

    class Meta:
        form_class = ProductForm

    def resolve_product(self, info, **kwargs):
        return self


class UpdateApplication(DjangoModelFormMutation):

    application = graphene.Field(ApplicationType)

    class Meta:
        form_class = ApplicationForm


class CreateAmountMutation(DjangoCreateMutation):
    class Meta:
        model = Amount
        login_required = True
        exclude_fields = ('order', )


class CreateOrderMutation(DjangoCreateMutation):
    class Meta:
        model = Order
        login_required = True
        exclude_fields = ('products', 'amount_set', 'user')
        many_to_many_extras = {
            "amount_set": {
                "add": {"type": "CreateAmountInput"}
            }
        }

    @classmethod
    def mutate(cls, root, info, **input):
        products = Product.objects.filter(display=True)
        options = Option.objects.all()
        weights = Weight.objects.all()

        application = Application.objects.get(
            id=input['input']['application'])

        order = Order.objects.get_or_create(
            user=info.context.user, application=application)

        amounts = input['input'].pop('amount_set_add')
        for amount in amounts:
            weight = weights.get(id=from_global_id(amount['weight'])[1])
            product = products.get(id=from_global_id(amount['product'])[1])

            if amount['option'] and product.options != Option.objects.none():
                option = options.get(id=from_global_id(amount['option'])[1])
                amount = Amount.objects.update_or_create(
                    product=product, option=option, weight=weight, order=order[0], defaults={'amount': amount['amount']})
            else:
                amount = Amount.objects.update_or_create(
                    product=product, weight=weight, order=order[0], defaults={'amount': amount['amount']})
        return {'order': order[0]}


class CreateOptionMutation(DjangoCreateMutation):
    class Meta:
        model = Option
        login_required = True


class CreateWeightMutation(DjangoCreateMutation):
    class Meta:
        model = Weight
        login_required = True
        permissions = ('application.add_weight', )


class UpdateProductMutation(DjangoUpdateMutation):
    class Meta:
        model = Product
        login_required = True


class Mutation(graphene.ObjectType):
    add_product = AddProduct.Field()
    create_order = CreateOrderMutation.Field()
    add_option = CreateOptionMutation.Field()
    add_weight = CreateWeightMutation.Field()

    update_application = UpdateApplication.Field()
    update_product = UpdateProductMutation.Field()


# Queries
# =========

class Query(graphene.ObjectType):
    all_applications = DjangoListField(ApplicationType)
    product = Node.Field(ProductType)
    application_products = DjangoFilterConnectionField(ProductType)
    all_options = DjangoFilterConnectionField(OptionType)
    all_weight = DjangoFilterConnectionField(WeightType)
    application_order = DjangoFilterConnectionField(OrderType)
    application_by_slug = graphene.Field(
        ApplicationType, slug=graphene.String())

    @login_required
    def resolve_application_by_slug(self, info, slug, *args, **kwargs):
        return Application.objects.get(slug=slug)

    @login_required
    @check_application_permission_by_slug('member')
    def resolve_all_options(self, info, *args, **kwargs):
        return Option.objects.all()

    @login_required
    @check_application_permission_by_slug('member')
    def resolve_application_products(self, info, *args, **kwargs):
        return Product.objects.all()

    def resolve_all_applications(self, info, *args, **kwargs):
        return Application.objects.all()

    @login_required
    @check_application_permission_by_slug('member')
    def resolve_all_weight(self, info, *args, **kwargs):
        return Weight.objects.all()

    @login_required
    @check_application_permission_by_slug('admin')
    def resolve_application_order(self, info, *args, **kwargs):
        return Order.objects.all()
