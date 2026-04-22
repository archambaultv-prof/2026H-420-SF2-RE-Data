# Comparaison des structures de données

Durée : 2 heures

## Objectifs

- Comparer expérimentalement les performances des structures de données vues en cours
- Mesurer le temps d'exécution des opérations principales en Python
- Déterminer le seuil à partir duquel les opérations deviennent perceptiblement lentes
- Créer des graphiques avec Matplotlib pour visualiser et interpréter les résultats

## Instructions

> [!NOTE]
> Vous pouvez utiliser l'intelligence artificielle pour vous aider à écrire le code de mesure et les graphiques Matplotlib.

### Étape 1 : Mesure des temps d'exécution (60 minutes)

- En groupes de 2 à 3 personnes, écrivez un script Python `comparaison.py` qui mesure
  le temps d'exécution des opérations suivantes pour **chaque structure** :
  - Insertion au **début**, au **milieu** et à la **fin** (selon ce que la structure permet)
  - **Suppression** d'un élément
  - **Recherche** (*lookup*) d'un élément

- Pour **chaque structure**, comparez lorsque possible deux versions :
  1. L'implémentation **faite à la main** en Python pur (celle des exercices précédents ou
     celle des notes de cours)
  2. La structure **équivalente de la bibliothèque standard** Python
     (`list`, `dict`, `collections.deque`, etc.)

  L'objectif est donc aussi de mesurer l'écart de performance entre un code Python pur et
  les structures natives, qui sont optimisées en C.

- Pour chaque opération, effectuez les mesures avec des tailles croissantes,
  par exemple : 100, 1 000, 10 000, 100 000, 1 000 000, ...

- Utilisez `time.perf_counter()` ou le module `timeit` pour mesurer les temps
  d'exécution.

- **Pour chaque opération sur chaque structure**, trouvez la taille minimale *n*
  à partir de laquelle l'opération prend environ 2 à 3 secondes. Consignez ces
  valeurs dans votre `README.md`.

> [!TIP]
> Vous pouvez utiliser le code Python des [notes de cours sur les structures de données](https://archambaultv-prof.github.io/programmation-python/docs/category/structures-de-donn%C3%A9es-3)
> pour les implémentations faites à la main.

### Étape 2 : Graphiques Matplotlib (50 minutes)

- Pour chaque opération mesurée, créez un graphique avec Matplotlib représentant
  le **temps d'exécution en fonction de la taille *n*** pour toutes les structures
  comparées sur le même graphique.

- Les graphiques doivent permettre de déterminer visuellement la nature de la
  relation : constante O(1), logarithmique O(log n), linéaire O(n), quadratique O(n²), etc.

- Le script doit **générer et sauvegarder automatiquement** les graphiques en
  images `.png` dans le dossier courant via `plt.savefig("nom_du_graphique.png")`.

- Rédigez un court `README.md` (10 à 15 lignes) résumant vos observations :
  - Quelle structure est la plus rapide pour chaque opération ?
  - Quel est l'écart de performance entre l'implémentation maison et la bibliothèque standard ?
  - La relation observée correspond-elle à la complexité théorique attendue ?

> [!IMPORTANT]
> Votre dossier de travail doit être `comparaison/<nom-du-groupe>` et doit contenir :
> - `comparaison.py` — le script de mesure et de génération des graphiques
> - `README.md` — le résumé de vos observations
> - Les images `.png` générées automatiquement par le script

### Étape 3 : Demande de tirage (pull request) (5 minutes)

- Une fois que votre groupe a terminé, une personne du groupe doit faire une
  demande de tirage (pull request) pour que les autres puissent voir votre
  travail.

### Étape 4 : Acceptation de la demande de tirage (pull request) (5 minutes)

- Votre professeur va accepter votre demande de tirage (pull request) une fois
  que vous avez mis à jour votre travail. Votre travail sera alors visible sur
  la branche principale du dépôt.
