### Définition de ce qu'est une pile
Pile est une structure de donnée où le dernier élément arrivé est le premier à sortir.

### Les opérations principales

- `.append()` permet d'ajouter un élement au sommet de la pile 
- `.pop()` permet d'enlever le dernier élément ajouté dans la pile

> [!NOTE]
> L'ajout d'une variable permet de récuperer l'élement qui a été retiré avec `.pop()`
> Exemple : element_retire = liste.pop()

- `pile[-1]` retourne l'élement au sommet de la pile sans le supprimer
- `len(pile)` retourne le nombre d'élement dans la pile
- `len(pile) == 0` vérifie si c'est vide ou non en retournant True ou False

> [!NOTE]
> La variable "pile" peut être remplacé par le nom de votre liste/pile

- `.clear()` supprime tous les élements d'une pile

### Avantages et désavantages de la pile

| Avantages | Désavantages |
| :--- | ---: |
| Utile pour programmer des calculatrices | La pile a un ordre spécifique de sortie, ce qui restreint l'accès aux élements |
| Rapide car `.append()` et `.pop()` vont chercher le premier élement de la pile | Python n'offre pas les piles dans son programme de base, il faut l'implémenter soi-même |

### Exemples d'utilisations

- Shunting-yard
    - Un algorithme qui permet de faire des opérations mathématiques de base (PEMDAS)
- Ctrl + Z
    - Une opération qui permet d'annuler la derniere action effectué

