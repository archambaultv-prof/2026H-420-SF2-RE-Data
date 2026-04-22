# class Eleve:
#     def __init__(self, nom, prenom, matricule):
#         self.nom = nom
#         self.prenom = prenom
#         self.matricule = matricule

#     def __lt__(self, other):
#         return self.matricule < other.matricule

#     def __eq__(self, other):
#         return self.matricule == other.matricule

# e1  = Eleve("Doe", "John", 123)
# e2  = Eleve("Smith", "Jane", 123)

class NoeudABR:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

class ABR:
    def __init__(self):
        self.racine = None

#     def inserer(self, valeur):
#         self.racine = self._inserer(self.racine, valeur)

    def _inserer(self, noeud, valeur):
        if noeud is None:
            return NoeudABR(valeur)

        if valeur < noeud.valeur:
            noeud.gauche = self._inserer(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droit = self._inserer(noeud.droit, valeur)

        return noeud

#     def chercher(self, valeur):
#         return self._chercher(self.racine, valeur)

#     def _chercher(self, noeud, valeur):
#         if noeud is None:
#             return False
#         if valeur == noeud.valeur:
#             return True
#         elif valeur < noeud.valeur:
#             return self._chercher(noeud.gauche, valeur)
#         else:
#             return self._chercher(noeud.droit, valeur)

#     def minimum(self):
#         if self.racine is None:
#             raise ValueError("L'arbre est vide")
#         noeud = self.racine
#         while noeud.gauche is not None:
#             noeud = noeud.gauche
#         return noeud.valeur

#     def maximum(self):
#         if self.racine is None:
#             raise ValueError("L'arbre est vide")
#         noeud = self.racine
#         while noeud.droit is not None:
#             noeud = noeud.droit
#         return noeud.valeur

#     def supprimer(self, valeur):
#         self.racine = self._supprimer(self.racine, valeur)

#     def _supprimer(self, noeud, valeur):
#         if noeud is None:
#             return None

#         if valeur < noeud.valeur:
#             noeud.gauche = self._supprimer(noeud.gauche, valeur)
#         elif valeur > noeud.valeur:
#             noeud.droit = self._supprimer(noeud.droit, valeur)
#         else:
#             if noeud.gauche is None:
#                 return noeud.droit
#             if noeud.droit is None:
#                 return noeud.gauche

#             successeur = noeud.droit
#             while successeur.gauche is not None:
#                 successeur = successeur.gauche

#             noeud.valeur = successeur.valeur
#             noeud.droit = self._supprimer(noeud.droit, successeur.valeur)

#         return noeud

#     def parcours_en_ordre(self):
#         return self._parcours_en_ordre(self.racine)

#     def _parcours_en_ordre(self, noeud):
#         if noeud is None:
#             return []
#         return (
#             self._parcours_en_ordre(noeud.gauche)
#             + [noeud.valeur]
#             + self._parcours_en_ordre(noeud.droit)
#         )

#     def __repr__(self):
#         return str(self.parcours_en_ordre())