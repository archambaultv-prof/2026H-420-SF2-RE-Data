class Pile:

    def __init__(self, capacite=None):

        self.elements = []
        self.capacite = capacite

    def empiler(self, element):

        if self.capacite is not None and len(self.elements) >= self.capacite:
            raise OverflowError("La pile est pleine.")
        self.elements.append(element)

    def depiler(self):
 
        if self.est_vide():
            raise IndexError("La pile est vide.")
        return self.elements.pop()

    def sommet(self):

        if self.est_vide():
            raise IndexError("La pile est vide.")
        return self.elements[-1]

    def est_vide(self):

        return len(self.elements) == 0

    def est_pleine(self):

        if self.capacite is None:
            return False
        return len(self.elements) >= self.capacite

    def taille(self):
        return len(self.elements)

    def __str__(self):
        return f"Pile: {self.elements}"