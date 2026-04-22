class Node:
    def __init__(self, donnee):
        self.donnee = donnee
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ajouter_au_debut(self, donnee):
        nouveau_noeud = Node(donnee)
        nouveau_noeud.next = self.head
        self.head = nouveau_noeud
    
    def afficher(self):
        tete = self.head
        while tete is not None:
            print(tete.donnee, end=" -> ")
            tete = tete.next
        print("None")
    
    def longueur(self):
        nombre_elements = 0
        tete = self.head
        while tete is not None:
            nombre_elements += 1
            tete = tete.next
        return nombre_elements