class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None

    def insert_gauche(self, valeur):
        if isinstance(valeur, ArbreBinaire):
            # Si c'est un nœud existant, l'attacher directement
            self.enfant_gauche = valeur
        else:
            # Si c'est une valeur simple, créer un nouveau nœud
            if self.enfant_gauche == None:
                self.enfant_gauche = ArbreBinaire(valeur)
            else:
                new_node = ArbreBinaire(valeur)
                new_node.enfant_gauche = self.enfant_gauche
                self.enfant_gauche = new_node

    def insert_droit(self, valeur):
        if isinstance(valeur, ArbreBinaire):
            # Si c'est un nœud existant, l'attacher directement
            self.enfant_droit = valeur
        else:
            # Si c'est une valeur simple, créer un nouveau nœud
            if self.enfant_droit == None:
                self.enfant_droit = ArbreBinaire(valeur)
            else:
                new_node = ArbreBinaire(valeur)
                new_node.enfant_droit = self.enfant_droit
                self.enfant_droit = new_node

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.enfant_gauche

    def get_droit(self):
        return self.enfant_droit
    def supprimer_gauche(self):
        self.enfant_gauche = None
    def supprimer_droit(self):        
        self.enfant_droit = None
    def hauteur(self):
        if self is None:
            return 0
        else:
            hauteur_gauche = self.enfant_gauche.hauteur() if self.enfant_gauche else 0
            hauteur_droit = self.enfant_droit.hauteur() if self.enfant_droit else 0
            return max(hauteur_gauche, hauteur_droit) + 1
    def minimum(self):
        if self.enfant_gauche is None:
            return self.valeur
        else:
            return self.enfant_gauche.minimum()
    def maximum(self):
        if self.enfant_droit is None:
            return self.valeur
        else:
            return self.enfant_droit.maximum()
bob = ArbreBinaire(10)
Robert = ArbreBinaire(20)
René = ArbreBinaire(5)
René.insert_gauche(11)
bob.insert_gauche(René)
bob.insert_droit(Robert)
Robert.insert_droit(25)
print(bob.get_valeur())  # Affiche 10
print(bob.minimum())  # Affiche 5
print(bob.maximum())  # Affiche 25
print(bob.hauteur())  # Affiche 3