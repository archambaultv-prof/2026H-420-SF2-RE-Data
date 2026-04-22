# arbres binaires 
> Structure dans laquelle chaque élément ne peut qu'avoir deux enfants, un à droite et l'autre à gauche, ce qui donne une certaine structure conditionnelle où chaque choix te mène vers un chemin différent.

## Opérations principales 

### Search 
Trouver un élément de l'arbre en utilisant une structure conditionelle
qui donne le parent et les deux enfants.

### Insert 
Ajouter un élément dans l'arbre en utlisant une structure conditionelle 
qui repère le parent et ajoute un enfant.

### Delete
Supprimer un élément de l'arbre dépendant de sa position dans l'arbre :
- Pas d'enfants : on le supprime direct
- Un enfant : on le remplace 
- Deux enfants : on le remplace par le plus petit à droite 

### Parcours 
lire tous les éléments de manières différentes :
- Inorder (Infix) : Gauche, Racine, Droite (Donne les valeurs triés)
- Preorder (Préfixe) : Racine, Gauche, Droite (Utile pour copier un arbre)
- Postorder (Postfix) : Gauche, Droite, Racine (Utile pour supprimer un arbre)

### Height 
Sert à connaître le nombre total de noeuds dans un arbre.

### Minimum/Maximum
Trouver la plus petite ou la plus grande valeur d'un élément dans un arbre.

# Avantages 
- Recherche beaucoup plus vite qu'une liste et surtout pour un volume de données massif.
- Insetion beaucoup plus vite qu'une liste et surtout pour un volume de données massif.
- Supression beaucoup plus vite qu'une liste et surtout pour un volume de données massif.
- Structure hiérarchique naturelle contrairement aux tableaux.
- Taille dynamique contrairement aux tableaux avec une structure prédéfinie, ce qui permet de modifier le volume de données.
- Tri automatique grâce à infix ce qui permet de sortir les données triées sans éfforts.

# Désavantages 
- Déséquilibrer en insérant un suite d'éléments déjà trié, ce qui fait que chaque nouveau noeud seras l'enfant droit du précédent ce qui détruit la structure d'arbre et se transforme en un simple liste droite.
- Pas d'accès direct à un élément de l'arbre, contrairement à un tableau où l'on peut accéder à un élément instantanément, dans un arbre, on doit toujours partir de la racine et descendre les niveaux. L'accès aléatoire est impossible.
- Il est beaucoup plus compliquer de supprimer un élément d'un arbre, car les enfants doivent toujours être remplacés pour conserver la structure d'arbre.

# Exemple d'utilistion 
```python
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

class ArbreBinaireRecherche:
    def __init__(self):
        self.racine = None

    def inserer(self, valeur):
        if self.racine is None:
            self.racine = Noeud(valeur)
        else:
            self.inserer_2(valeur, self.racine)

    def inserer_2(self, valeur, noeud):
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Noeud(valeur)
            else:
                self.inserer_2(valeur, noeud.gauche)
        else:
            if noeud.droit is None:
                noeud.droit = Noeud(valeur)
            else:
                self.inserer_2(valeur, noeud.droit)

        # vide? oui = nouv noeud avec la valeur donnée, Else : _inserer pour trouver la position correcte dans l'arbre et insérer le nouveau noeud 
    
    def chercher(self, valeur):
        return self.chercher_2(valeur, self.racine)

    def chercher_2(self, valeur, noeud):
        if noeud is None or noeud.valeur == valeur:
            return noeud is not None
        if valeur < noeud.valeur:
            return self.chercher_2(valeur, noeud.gauche)
        return self.chercher_2(valeur, noeud.droit)

        # vide? oui = False, Else : structure conditionelle pour trouver élément 

    def parcourir_infix(self) :
        return self.parcourir_infix_2(self.racine)
```
**Pas eu le temps de finir**


   