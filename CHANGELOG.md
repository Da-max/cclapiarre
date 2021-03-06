# Changements
Tous les changements de ce projet sont documentés ici, ce fichier est affiché sur cette page : [https://cclapiarre.deblan.fr/changements/](https://cclapiarre.deblan.fr/changements/) il est donc écrit en français.

## 4 octobre 2020 : Sortie de la version 5.5.0
### Ajout
* Ajout d’une interface permettant de créer, de supprimer ou de modifier des utilisateurs.

### Résolution de bogue
* Des corrections ont été faites sur le système de modification et d’ajout des agrumes. Le système de pagination a été retiré.

### Modification
* Les permissions des pages permettant de commander des agrumes ou du café ont été modifiées ce qui permet de voir les pages sans pour autant accepter les commandes.
* Le bas de page a été modifié afin de prendre en compte les récentes modifications de status du groupe de court-circuit La Piarre, qui n’est, désormais, plus rattaché à l’association court-circuit mais à l’association court-circuit Buëch Méouge.

## 22 avril 2020 : Sortie de la version 5.4.5
### Ajout
* Ajout d’une fonctionnalité permettant de modifier ou de supprimer un produit pour la commande d’agrumes.
* Il est également possible de modifier les status des produits directement depuis la page listant les produits.


## 12 avril 2020 : Sortie de la version 5.4.4

### Ajout
* Développement d’un système déjà existant : la règle d’accès aux différentes pages du site. Ce système intègre désormais les options suivantes :
  * La possibilité de définir une date et une heure à laquelle cette règle prendra effet.
  * Ajout d’une option permettant de rendre la page introuvable (404), si cette option n’est pas activée, un simple message sera affiché dans une fenêtre modale.
  * Possibilité de personnaliser le message affiché dans la fenêtre modale (ce message sera affiché uniquement si l’option « lever une exception » n’est pas activée).
* Des tests ont été ajoutés afin de tester cette nouvelle fonctionnalité.

### Résolution de bogue
* Des petites corrections ont été effectués sur le système d’ajout de café (corrections de fautes d’orthographes).

## 04 avril 2020 : Sortie de la version 5.4.3

### Ajout
* Lors d’une commande de café, si un adhérent rentre **exactement** la même adresse mail OU le même numéro de téléphone que lors de sa première commande, il va lui être automatiquement proposé de changer sa commande par la nouvelle.
* Des tests ont été ajoutés afin de vérifier que l’api du système de commande de café fonctionne bien.

### Modification
La page permettant de commander du café utilise à présent l’api créée par Django rest framework.

### Résolution de bogue
* Résolution d’un bogue d’affichage des évènements (dû au framework UIkit) sur la page d’accueil.
* Correction d’un problème de sécurité permettant à un utilisateur *connecté uniquement* d’avoir accès à des pages dont il n’avait pas la permission (ce défaut était dû à la récente introduction de Django rest framework dans le projet). 

## 22 mars 2020 : Sortie de la version 5.4.2

### Modification
* Modification complète de la page listant les commandes de café, à présent, sur cette page, il est possible de :
  * Modifier une commande.
  * Supprimer cette commande.
  * Supprimer toutes les commandes.
  * Les anciennes fonctionnalités sont conservés (export de la liste au format PDF).

### Ajout
* L’application café possède désormais une api généré par Django rest framework, pour le moment ce système n’est utilisé que pour la nouvelle page de liste de commande, cette api devrait être utilisé pour la page de commande dans un futur proche.

## 10 mars 2020 : Sortie de la version 5.4.1

### Résolution de bogue
Modification de l’affichage du menu sur les petits écrans (téléphones), en effet, un bogue d’affichage empêcher cet affichage.

##  03 mars 2020 : Sorite de la version 5.4.0

### Modification

* Afin de faciliter la communication entre l'utilisateur, et plus particulièrement les parties utilisant le framework VueJs, le site intègre désormais une api qui, pour l’instant, ne concerne que la partie commande d’agrumes.
* L’application permettant de commander des agrumes a donc changé de système, désormais, elle utilise l’api (généré par [Django_rest_framework](https://www.django-rest-framework.org))

### Ajout

* La partie commande d’agrumes permet désormais, à certains utilisateurs, de modifier ou de supprimer de les commandes des utilisateurs. *Attention, une fois une commande supprimer, aucun retour en arrière ne sera possible.*
* **Ces fonctionnalités sont toujours à l’état de test, n’hésitez pas à me faire vos retours et à me signaler toutes erreurs.**

## 1 mars : Sortie de la version 5.3.2

### Correction de bug
Un bug dans le système de commande d’agrumes a été corrigé. En effet, lorsque l’on cliquait sur un bouton afin de voir les détails d’un produit, la page s’actualisait créant une erreur.

### Ajout
Les tests se généralisent plusieurs parties du site (Agrumes et Café).

### Modification
Modification dans l’organisation du fichier CHANGELOG.md (les changements les plus récents se trouvent désormais en haut du fichier).

## 24 février : Sortie de la version 5.3.1

### Ajout
* Un fichier (CHANGELOG.md) a été ajouté au projet afin de lister les changements fait au site. Ce fichier est affiché sur le site à cette adresse : [https://cclapiarre.deblan.fr/changements](https://cclapiarre.deblan.fr/changements).
* Une nouvelle dépendance s’ajoute donc au site : [https://github.com/trentm/django-markdown-deux](https://github.com/trentm/django-markdown-deux) afin de pouvoir afficher du Markdown dans le site.
* Le site inclus maintenant un système d’intégration continue, cela permet de tester automatiquement le projet à chaque mise à jour.
* Le site utilise maintenant [Font awesome](https://fontawesome.com) afin d’afficher des icônes dans les pages (l’icône de Gitlab provient de fontawesome).
* Le site inclus de plus en plus de tests afin d'être certain que l’ensemble du site fonctionne correctement.

### Modification
* Le footer a été modifié afin d’afficher plus d’informations à propos du site tel qu’un lien vers le code source du projet (hébergé par Gitlab), le numéro de la version du site, la licence de site ou le nom du développeur du site.
* Jusqu’à maintenant, le site utilisé un CDN afin de récupérer le framework css UIkit. Depuis la version 5.3.1, le style est directement inclus dans le site, cela favorisera son indépendance.
* La licence a été modifiée afin qu’elle soit plus en accord avec le projet (elle reste libre).


## 12 janvier : Sortie de la version 5.3
*Une page pour commander des pâtes, et plus de stabilité*

### Ajout
* En ce début d’année, un nouveau système fait son arrivée, la commande de pâtes. Ce système devrait donc faciliter les prochaines commandes de pâtes.
* Des tests sont intégrés à ce projet afin de sécuriser et de vérifier que le site fonctionne comme il le devrait.

### Correction de bogue
Modification du système permettant de générer le fichier récapitulatif de la commande de café.


## 23 décembre 2019 : Sortie de la version 5.2.1
*Une nouvelle fonctionnalité pour la commande d’agrumes, et une correction de bug !*

### Ajout
Pour cette fin d’année le site se dote d’une petite fonctionnalité en plus, en effet lors de la prochaine commande d’agrumes, les adhérents pourront choisir (ou pas) de recevoir un mail récapitulatif de leur commande.

### Résolution de bogue
La fonctionnalité permettant de télécharger le fichier récapitulatif de la commande d’agrumes a aussi été revu, tout devrait à présent fonctionner.

## 09 novembre 2019 : Sortie de la version 5.2
*Du dynamisme arrive sur le site !*

### Ajout
* Depuis cette version, le site utilise le framework frontend [vuejs](https://vuejs.org) afin de rendre le site plus dynamique. Cette technologie est utilisée pour le moment uniquement pour les parties agrumes et café !
* Ajout d’un fil d’Ariane afin de naviguer plus facilement dans le site.

## 11 septembre 2019 : Sortie de la version 5.1.1
Petite correction de la liste des commandes de café.


## 30 août 2019 : Sortie de la version 5.1
*Ajout d’une grosse partie du site : les commandes de café et refonte stylistique.*

### Ajout
* Le site intègre désormais toute une partie d’administration afin d’ajouter, de supprimer et de modifier les cafés.
* En plus de pouvoir commander des agrumes, le site permet également de commander des cafés.

### Modification
* Le fond a également changé de couleur pour une meilleure lisibilité.
* L’animation d’apparition du “footer” (la panel tout en bas) a également changé afin d’offrir une meilleure navigation dans le site.


## 30 juillet 2019 : Sortie de la version 5.0

### Modification
* Le site change de design, il utilise dès à présent le framework CSS [UIkit](https://getuikit.com)
* Le langage utilisé côté serveur change également, ce projet utilise maintenant le [Python](https://www.python.org/) et le framework [Django](https://www.djangoproject.com/) (avant cette version, le site utilisé du [PHP](https://php.net))
* Le nom de domaine du site a également changé. Depuis cette version, l’hébergeur du site est [Deblan](https://deblan.io), cet hébergeur fait partie des [CHATONS](https://www.chatons.org/). Collectifs Hébergeurs, Alternatifs, Transparents, Ouverts, Neutres et Solidaires). Ils s’engagent à garder vos données confidentielles, à ne pas utiliser de régies publicitaires, BREF il s’agit d’hébergeurs éthiques.