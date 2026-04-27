Définition
Une liste chaînée est une structure de données linéaire composée de noeuds  reliés entre eux. Chaque noeud contient :

Une valeur
Un pointeur vers le noeud suivant

Insérer en tete -> Ajouter un noeud au début de la liste
Insérer en queue -> Ajouter un noeud à la fin de la liste
Supprimer -> Retirer un noeud de la liste
Rechercher -> Trouver un noeud contenant une valeur donnée
Parcourir -> Afficher tous les noeuds de la liste
Taille -> Retourner le nombre de noeuds

Avantages

Insertion et suppression efficaces : en tête de liste, sans déplacement d'éléments
Taille dynamique : La liste peut grandir ou rapetisser à l'exécution, sans taille fixe
Pas de gaspillage mémoire : On utilise uniquement ce dont on a besoin

Inconvénients

Accès séquentiel uniquement : Pour accéder au éléments, on doit parcourir depuis le début 
Utilisation mémoire supplémentaire : Chaque noeud stocke un pointeur en plus de la valeur

En informatique

Piles et files  : Implémentées naturellement avec des listes chaînées
Historique de navigation : Les boutons « Précédent » et « Suivant » d'un navigateur utilisent une liste doublement chaînée