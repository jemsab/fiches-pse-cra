# Les CMS - Systèmes de gestion de contenu

Écrire une page web vitrine pour une société, une association ou tout autre projet est une démarche importante de nos jours. 
Cependant dès lors que l'on commence à multiplier les articles ou pages, cela devient vite ingérable.

La solution se trouve dans les systèmes de gestion de contenu (CMS en anglais).

## Composants d'un CMS classique

Traditionnellement les CMS sont composés de trois élements : 

* Un éditeur permettant d'ajouter du contenu, de le categoriser et de le publier.
* Un système de persistence du contenu, souvent assuré par la connexion à une base de données
* Un moteur de rendu, ou template engine en anglais, permettant de prendre le contenu et de l'afficher.

## Différences avec un CMS headless

Un système de gestion de contenu découplé ne dispose pas de la fonctionnalité de rendu du contenu.
Désormais c'est au client d'afficher le contenu en fonction de ses propres spécificités.

Le retrait de cette fonctionnalité offre deux principaux avantages : 

* Le CMS est plus léger et moins gourmand en ressources
* Le contenu peut être utilisé sur n'importe quel client, à condition que celui-ci puisse récupérer les données du CMS (le plus souvent un appel REST).
On découple le gestionnaire du contenu de l'affichage. Cela permet une plus grande flexibilité quant au client.

Un désavantage est que l'on doit développer un client pour chaque appareil où le contenu est affiché.
Cet inconvénient est attenué par l'utilisation de technologies web, qui permettent un affichage responsive sur tous les appareils dotés de navigateur web.
