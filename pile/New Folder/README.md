# Dossier pour les exercices sur les piles
- Une pile dans le structure de donné est un type de données abstrait qui sert comme une collection composé de deux éléments: Push et pop.\
    - Push :
  La fonction Push sert d'entrer une donnée dans la collection. Ceci est ajouter à la fin de celle-ci.

    - Pop :
  La fonction Pop sert comme un accesseur aux données, qui retourne la dernière valeur ajoutée.

- Avantage et inconvénient:
    - Avantage : Accès facile et rapide des données.
    - Inconvénient : L'accès est limité à la dernière donnée ajoutée.

- Exemples d'utilisation :
    - Gestion de l'historique de navigation : Les navigateurs web utilisent une pile pour stocker les pages visitées. Cliquer sur le bouton "Précédent" revient à dépiler (pop) la dernière URL pour afficher la précédente.

    - Fonction "Annuler" (Undo/Redo) : Dans les logiciels de traitement de texte ou de retouche d'image, chaque action est empilée. L'annulation retire l'action la plus récente du sommet de la pile.

     - Appels de fonctions (Call Stack) : C'est l'utilisation la plus fondamentale en programmation. Lorsqu'une fonction en appelle une autre, l'adresse de retour et les variables locales sont empilées pour être récupérées une fois la fonction terminée.

    - Évaluation d'expressions arithmétiques : Les piles permettent de convertir et de calculer des expressions en notation polonaise inverse (NPI) ou de transformer une notation infixe en postfixe.

    - Vérification de l'appariement des parenthèses : Les compilateurs utilisent une pile pour s'assurer que chaque parenthèse, crochet ou accolade ouverte est correctement fermée dans le bon ordre.

    - Algorithmes de parcours de graphes (DFS) : Le parcours en profondeur d'abord (Depth-First Search) utilise une pile (explicite ou via la récursion) pour garder trace des nœuds à explorer.

    - Inversion de données : Puisque le dernier élément entré est le premier sorti, une pile est l'outil le plus simple pour inverser une chaîne de caractères ou une liste.

    - Algorithmes de "Backtracking" : Utilisé pour résoudre des puzzles (comme le Sudoku ou la sortie d'un labyrinthe), où l'on empile les chemins explorés pour pouvoir revenir en arrière en cas d'impasse.