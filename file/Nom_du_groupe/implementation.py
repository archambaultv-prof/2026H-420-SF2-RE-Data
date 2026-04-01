class File:
    def __init__(self, base_de_donnee):
        self.base_de_donnee = base_de_donnee
    
    def est_vide(self):
        if len(self.base_de_donnee) == 0:
            return True
        return False
    
    def enqueue(self, valeur):
        self.base_de_donnee.append(valeur)

    def dequeue(self):
        if self.est_vide():
            return "Erreur: La file est vide"
        else:
            self.base_de_donnee.pop(0)
    
    def size(self):
        return len(self.base_de_donnee)

    def front(self):
        if self.est_vide():
            return "Erreur: La file est vide"
        else:
            return self.base_de_donnee[0]