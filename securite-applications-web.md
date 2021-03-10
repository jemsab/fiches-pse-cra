# Sécurité des applications web

La "webisation" des applications des administrations, aussi bien à  destination des agents que du grand public apporte beaucoup d'avantages.
D'un côté, on obtient une plus grande facilité de déploiement, des mises à jour plus rapides, une interface plus ergonomique, etc.
Malheureusement, de l'autre côté, cela introduit de nombreux risques ayant des conséquences potentiellement désastreuses pour une administration.

Afin de répondre à la question comment faire face aux risques de ce nouveau genre d'application : 
Il convient de comprendre ces risques avant d'y répondre avec des solutions concrètes.

## I. Enjeux

- Vol de données utilisateurs

	- Injection SQL : 
			Exécution de code sql directement depuis une saisie utilisateur.
	
	- Vol de cookies
			Sur une session non-chiffrée, les cookies contenant des données sensibles peuvent être interceptés

- Usurpation d'identité

	- CSRF :
			Appel d'un formulaire web d'un site A depuis un site B
  
	- XSS :
			Insertion sur une page du code js qui sera lu à l'affichage de la page par les utilisateurs

- Au-delà de l'application

	- Pivot d'attaque :
			Une application vulnérable peut être utilisé comme pivot pour exploiter d'autres
	
	-  Perte de confiance / réputation :
	 		La confiance des utilisateurs est primordiale, le détournement de leur navigateur pour du cryptomining porte atteinte à cette confiance

## II. Solutions 

- Solutions intégrées aux navigateurs

	- Liaison avec le serveur : 
			 CORS empêche l'envoi de formulaire à une serveur qui ne l'aurait pas préalablement autorisé et https (authenticité, confidentialité et intégrité des échanges)
	
	- Protection des cookies : 
			Mécanismes httpOnly et samesite empêche la lecture des cookies par d'autres pages, localStorage

- Solutions dans l'application

	- Retraitement de tout saisie utilisateur :
			Retirer les balises html pour le js, empêcher l'exécution de la saisie utilisateur par la BDD

	- Hashage et salting de la base de données
			Les mots de passe ne doivent pas être stockés en clair

- Solutions hors application

	- Protection réseau : 
			Isolation de l'application (VLAN, DMZ, Reverse-proxy)

	- Protection physique :
			Contrôle accès salles serveurs, datacenter 

En conclusion, les démarches proposées permettent de répondre à un bon nombre d'attaques. 
La sécurité en informatique doit se concevoir comme un onion avec des couches, le renforcement de chaque couche permettra la sécurisation de l'ensemble.

Pour aller plus loin, il faut évoquer le sujet de l'humain, le premier vecteur d'attaque des SSI, il conviendrait de mettre en place des solutions de formation et d'information, 
à destination des agents et des utilisateurs pour une meilleure sécurité.

