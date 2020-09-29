from graphene import ObjectType, Schema

from article.schema import Query as article_query, Mutation as article_mutation
from carousel.schema import Query as carousel_query


class Query(article_query, carousel_query, ObjectType):
    pass


class Mutation(article_mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
