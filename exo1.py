#!/usr/bin/python
# coding: utf8 

# initialisation des listes
Liste1=[1,5,7,14,50,100,150]
Liste2=[1,2,3,10,13,15,200]

# L'objectif de l'exercice est de classer par ordre croissant les valeurs contenues dans les listes 1 et 2

Liste3=[]

print "Liste1 : ",Liste1
print "Liste2 : ",Liste2

# Initialisation des compteurs
i=0
j=0

# tant que les indices i et j sont inférieurs au longueurs respectives de Liste1 et liste2
while i<len(Liste1) and j<len(Liste2):
   if Liste1[i]<Liste2[j]:
       Liste3.append(Liste1[i])
       i=i+1
   else:
       Liste3.append(Liste2[j])
       j+=1
# si i ou j sont en fin de liste  on sort de la première boucle

# Si le parcours de la liste1 n'est pas terminé alors on affiche toutes les valeurs restant dans la liste1
# Sinon on entre pas dans la boucle
while i<len(Liste1):
    Liste3.append(Liste1[i])
    i+=1

# Si le parcours de la liste2 n'est pas terminé alors on affiche toutes les valeurs restant dans la liste2
# Sinon on n'entre pas dans la boucle
while j<len(Liste2):
    Liste3.append(Liste2[j])
    j+=1

# Affichage du résultat
print "Liste3 : ", Liste3
