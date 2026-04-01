class Pile:
    def __init__(self, liste):
        self.liste = liste

    def ajouter(self, element): #ajoute un élément au sommet de la pile
        self.liste.append(element)
        return self.liste

    def retirer(self): #retire l'élément du sommet de la pile
        if len(self.liste) == 0:
            return "La pile est vide"
        else:
            return self.liste.pop()