Une file est une structure de donnée qui ressemble à une liste.
Les files ont un nombre maximal de places.
Lorsqu'une file atteint son nombre maximal d'items elle suprime le premier ajouté.

Les opérations principales:
-Ajouter un élement a le file -> push
-Retirer un élément de la file -> pop
-Tester si la file est vide -> est_vide
-Calculer la longueur de la file -> taille
-Renvoyer la file sous la forme de chaine de caractères -> __str__
-Renvoyer le minimum et le maximum de la file ->min et max
-Rechercher un élément dans la file -> trouver
-réinitialiser la file -> réinitialiser

Avantages:
-taille prédéterminée
-plus facile à ordonne
-ordre prédéterminé

Inconvénients:
-Accès restreint, impossible d'acceder a un élément en milieu de liste sans suprimer ceux avant
-Accéder au dernier élément necessite de parcourir toute la structure

Exemple d'utilisations:
-Pour gérer l'ordre de passage d'élèves pour une présentation