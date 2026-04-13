class Pile:

    def __init__(self, pile):
        self.pile = pile

    def push(self, element): # ajoute un élement au sommet de la pile
        self.pile.append(element)
    
    def pop(self): # enleve le dernier élément ajouté dans la pile
        self.pile.pop()

    def peek(self): # retourne l'élement au sommet de la pile sans le supprimer
        if len(self.pile) == 0: # Vérifie si la liste est vide ou pas
            pass
        else:
            return self.pile[-1]
    
    def size(self): # retourne le nombre d'élement dans la pile
        return len(self.pile)

    def IsEmpty(self): # vérifie si c'est vide ou non en retournant True ou False
        return len(self.pile) == 0

    def Vider(self): # supprime tous les élements d'une pile
        self.pile.clear()
