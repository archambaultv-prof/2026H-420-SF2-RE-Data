# permet dinstencier la taille maximale de la file si l'utilisateur ne la rentre pas
import sys

class File:
    def __init__(self, max_size = None):
        #Si l'utilisateur ne rentre pas de taille maximale, on met la taille maximale à l'infini (sys.maxsize)
        self.max_size = sys.maxint if max_size == None else max_size
        self.elements = []
    #lis le readme :3 uwu
    def push(self, element):
        if type(element) is list:
            for i in element:
                if len(self.elements) < self.max_size:
                    self.elements.append(i)
                else:
                    break
        else:
            if len(self.elements) < self.max_size:
                self.elements.append(element)
            else:
                raise IndexError("La file est pleine")
    def pop(self):
        if len(self.elements) == 0:
            raise IndexError("La file est vide")
        self.elements.pop(0)
    def prochain_élément_a_pop(self):
        return self.élements[0]
    def est_vide(self):
        return len(self.elements) == 0
 
    def taille(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)
    def min(self):
        return min(self.elements )
    def max(self):
        return max(self.elements)
    def trouver(self, element):
        return self.elements.index(element)
    def réinitialiser(self):
        self.elements = []

bob = File(3)
bob.push(1)
bob.push(["caca", "Bryan"])
print(bob)
bob.pop()
print(bob)