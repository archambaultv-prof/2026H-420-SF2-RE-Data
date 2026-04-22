class chaine:
    def __init__(self, valeur, pointeur=None):
        self.valeur = valeur
        self.pointeur = pointeur


class Liste_Chaine:
    def __init__(self,valeur,pointeur):
        self.valeur = valeur
        self.pointeur = pointeur

    def taille(self):
        longeur = 0
        if self.pointeur is not None:
            self.poiteur.taille
        longeur += 1
        return longeur

    def recherche_index(self, element, iteration=0):
        if self.valeur == element:
            return iteration
        if self.pointeur is not None:
            self.pointeur.recherche_index(element, iteration + 1)

    def recherche_valeur(self,index):
        if index > self.taille():
            return False
        for posi in range(index):
            if posi == index:
                return self.valeur
            self.pointeur.recherche(index)

    def supprimer(self,valeur):
        pass 

