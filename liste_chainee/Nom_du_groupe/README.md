# Liste chainée
## Définition 

Une liste chainée est une structure de données contenant des éléments ordonnés qui contiennent une valeur et un pointeur vers l'élément suivant. Cette structure de données permet une addition et une supression de données plus efficace qu'avec une liste normale, surtout lorsque la valeur est au début ou au milieu de la liste. Cependant, l'accès aux données est plus lent. Il est possible de faire des listes chaînées circulaires (où le dernier élément pointe vers le premier) ou à double lien (où chaque élémengt possède un pointeur qui pointe vers l'élément suivant et un qui pointe vers le précédent).

## Opérations principales

- first_add(knot) : ajouter un élément au début de la liste
- last_add(knot) : ajouter un élément à la fin de la liste
- add(knot) : ajouter un élément au milieu de la liste
- length() : len mais pour une liste chainée
- is_first(knot) : check if first
- is_last(knot) : check if last
- pointer_first(knot) : transforme le noeud en le premier élément de la liste
- pointer_last(knot) : transforme le noeud en le dernier élément de la liste
- remove(knot) : enlever un neoud peu importe ou il est dans la liste
- search(value) : regarde si la valeur fournie est dans la liste

## Avantages / Inconvénients

### Avantages
- L'insertion et la suppression d'un élément est facile et ne nécessite pas le recopiage de la liste chaînée au complet, seulement le changement de quelques pointeurs.
- La taille de la liste chaînée peut varier grandement sans avoir à réajuster tout un tableau.
- Aucune mémoire n'est allouée à prévoir de la place pour de nouveaux éléments (contrairement aux listes, qui doivent prévoir un espace mémoire contiguë pour pouvoir rajouter des éléments).

### Inconvénients
- Pour accéder à un élément de la liste, il faut parcourir la liste depuis le début jusqu'à l'élément, ce qui peut être très long.
- Les listes chainées sont à risque de cache missses, ce qui force l'ordinateur à aller chercher l'information dans une mémoire plus lente.

## Applications
- Manipulation de polynomes
- Cryptographie (manipulation de gros nombres)
- Symulation de système de particules

## Sources 
- Reddit
- Hazelcast
- Datacamp
- Wikipédia
- Gemini