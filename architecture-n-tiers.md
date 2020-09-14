# L'architecture N-Tiers

Un projet informatique simple nécessite une organisation de code simple. En effet, pour un programme très simple un seul fichier ou module est souvent nécessaire. 

Cependant, avec l'ajout de fonctionnalités, d'intervenants, et plus globalement au cours de sa vie, un projet devient rapidement ingérable dans un bloc monolithique. 
Il convient alors de séparer l'application dans un ensemble de sous-modules qui communiquent entre eux en respectant un contrat de services, on parle aussi d'API.

## Exemple typique : l'architecture trois-tiers ou MVC

Un format fréquent d'architecture n-tiers est la division d'une application en trois tiers ou couches :

* Présentation : L'écran ou interface présenté à l'utilisateur.
* Métier : Logique métier de traitements des informations
* Données : Permet l'accès à l'information persistente, en lecture ou en écriture

Cette division en trois est plus particulièrement utilisé pour la conception d'applications Web, on parle alors d'architecture Modèle-Vue-Contrôleur.
Le modèle correspond à la couche données, la vue à la couche présentation et le métier au contrôleur.

## Avantages

Cette séparation présente l'avantage principal d'augmenter la **maintenabilité** d'une application : 
tant que l'on respecte le contrat de services de la couche, on peut changer tout ce que l'on veut au sein d'une couche. 
*Par exemple, un programme qui affiche la liste des candidats admis à un examen, 
on peut tout à fait changer les règles de calcul du résultat sans changer l'affichage de la page*

Cela permet aussi une plus grande **évolutivité** de l'application : on peut facilement intégrer de nouvelles modules en consommant l'API proposé par les modules déjà en plus. *Par exemple, aujourd'hui mon programme présente une page web que je souhaite conserver pour certains de mes clients mais je souhaite ajouter une autre version qui utilise les mêmes règles métier et les mêmes données, il me suffit alors de créer un nouveau sous-module qui peut s'appuyer sur les services existants*
