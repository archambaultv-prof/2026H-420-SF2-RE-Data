# La file 
## Définition

La file est une structure de donnée linéaire qui suit le principe de "first in, first out", donc les premiers éléments qu'on ajoute à la file sont aussi les premiers qu'on sort de la pile.

## Opérations principales

- enqueue(obj):
ajoute un objet (obj) à la fin de la file
- dequeue():
retire et retourne le premier objet de la file
- size():
retourne le nombre d'objets dans la file
- est_vide():
retourn True si la file est vide et False si il y a un ou plusieurs objets
- front():
retourne le premier objet de la file sans le retirer

## Avantages / Inconvénients

### Avantages:
- simple
- fiable pour effectuer les opérations dans un ordre logique. (réduit rissques d'erreurs)
### Inconvénients:
- suite fixe ne permet pas l'optimisation des tâches (les tâches les plus courtes ne sont pas nécessairement faites avant les tâches les plus longues)
- anomalie de Belady: plus le nombre d'objets dans la file est élevé, plus la performance en subit

## Applications 
- serveur d'impressions (comme on a ici à l'école)
- mémoriser des transactions à effectuer plus tard

**source: wikipédia**