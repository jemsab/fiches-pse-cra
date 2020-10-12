# AIDE MEMOIRE ALGO

Les lignes précédées d'un "//" sont des commentaires
Les lignes d'instructions se terminent par un ";"

## A- Les variables

    // Déclaration d'une variable
    SOIT maVariable de type Type; // par ex:[Booléen, Entier, Texte, Date, Réel etc...]

    // Affectation d'une variable
    maVariable <- Valeur;  // La valeur sera de type identique à celui déclaré


## B- LES STRUCTURES DE CONTROLE

### 1- Exécution conditionnelle d'instructions

		SI condition ALORS
			// Exécution des instructions suivantes si la condition est satisfaite)
			instruction 1;
			instruction 2;
		FIN SI;

		SI condition ALORS
			// Exécution des instructions suivantes si la condition est satisfaire) 
			instruction 1;
			instruction 2;
		SINON
			// Exécution des instructions suivantes si non-condition satisfaite)
			instruction 1;
			instruction 2;
		FIN SI;

### 2- LES BOUCLES
	
#### 1- Boucle POUR
		
		// La structure POUR est faite pour parcourir l'intégralité des valeurs d'un ensemble fini
		
		POUR CHAQUE element de ensemble FAIRE :
		// ensemble peut être une liste d'objets, d'entiers etc...
			instruction 1;
			instruction 2;
			instruction 3;
		FIN POUR;
		
#### 2- Boucle REPETER
		
		// La structure répéter impose au moins une exécution d'une liste d'instruction
		// Cette structure est souvent utilisé pour gérer les saisies clavier de l'utilisateur
	
		REPETER
			instruction 1;
			instruction 2;
			instruction 3;
		JUSQU'A condition 
		// La condition indiquée permet de sortir de la boucle
		
#### 3- Boucle TANT QUE
		
		// Les instructions contenues dans la boucle Tant que peuvent ne jamais être exécutées
		// si les conditions ne sont jamais réunies
		
		TANT QUE condition FAIRE :
			instruction 1;
			instruction 2;
			instruction 3;
		FIN TANT QUE;
			
### 3- Les CHOIX
	
		// Les choix peuvent être implémentés par des SI mais la majorité des langages implémentent la structure CASE
		
		SELON QUE maVariable :
			cas1 : 	instruction 1.1;
					instruction 1.2;
					instruction 1.3;
					
			cas2 :  instruction 2.1;
					instruction 2.2;
					instruction 2.3;
			...
			casN :  instruction n.1;
					instruction n.2;
			
			Autre : 
			// dans tous les autres cas exécution des instructions suivantes
					instruction a.1;
					instruction a.2;
		FIN SELON;

## C- Les méthodes

		// Regroupement d'instructions sous un nom générique.
		
		// Déclaration d'une méthode
		SOIT la méthode ma_Méthode( liste des Variables Typées )
		// Commentaire sur ce que fait la méthode et ce qu'elle renvoie (type de l'élément renvoyé)
			instruction 1;
			instruction 2;
			instruction 3;
			
			RETOURNER résultat ; // résultat est une variable
