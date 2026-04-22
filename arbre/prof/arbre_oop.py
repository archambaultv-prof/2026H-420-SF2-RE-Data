# from arbre import Node

# dossier = Node("dossier")
# fichier = dossier.add_child("fichier1")

# oups = fichier.add_child("oups")

class Fichier:
    def __init__(self, nom):
        self.nom = nom

class Dossier:
    def __init__(self, nom):
        self.nom = nom
        self.children = []

    def add_child(self, nom):
        node = Dossier(nom)
        self.children.append(node)
        return node

    def add_file(self, nom):
        file = Fichier(nom)
        self.children.append(file)
        return file
    
class Ami:
    def __init__(self, nom):
        self.nom = nom
        self.amis: list[str] = []