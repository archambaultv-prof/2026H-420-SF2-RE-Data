import json

class File:
    def __init__(self,filename="file/Nom_du_groupe/file.json"): 
        self.base_de_donnee = []
        self.index_tete = 0
        self.filename = filename
        self.load_file() #Pourquoi load_file est dans le constructeur?
                         #En mettant la fonction load_file dans le constructeur
                         #L'utilisateur n'a pas besoin de l'appeler pour que les données soient importées
    def load_file(self):
        """Méthode qui va rechercher dans un fichier une certaine base de donnée. \n
        Ne retourne rien, mais modifie les attributs self.base_de_donnee et self.index_tete. \n
        self.base_de_donnee --> La base de donnée obtenue dans le fichier. \n
        self.index_tete  --> L'index du premier "vrai" élément"""
        with open(self.filename, "r") as f:
            file = json.load(f)
        for i in file:
            self.base_de_donnee.append(i)
        self.index_tete = self.base_de_donnee[0]

    def est_vide(self) -> bool:
        """Methode qui evalue si une base de donnée File est "vide"."""
        if len(self.base_de_donnee) >= self.index_tete: 
            return False                      
        else:
            return True
            
    def enqueue(self, valeur):
        """Méthode qui ajoute un élément à la fin de la File"""
        self.base_de_donnee.append(valeur)

    def dequeue(self):
        """Fonction qui "retire" la tête de la File et la retourne."""
        if self.est_vide():
            return "Erreur: La file est vide"
        else:
            tete = self.base_de_donnee[self.index_tete]  #Que ce passe-t-il ici?
            self.base_de_donnee[self.index_tete] = None  #En gros, on retire le dernier élément en:
            self.index_tete += 1                         # le remplacant par None et en bougeant l'index 0 un peu plus loin.
            self.base_de_donnee[0] += 1                  #Si la liste est très grande, c'est inefficace de retirer et plus
            return tete                                  #efficace de remplacer.
    
    def size(self):
        """Méthode qui retourne la taille d'une file."""
        return len(self.base_de_donnee[self.index_tete :]) #Il ne faut pas oublier qu'on retourne 
                                                           #la taille de la File qu'on utilise.
    def front(self):
        """Méthode qui retourne le premier élément de la liste sans le retirer."""
        if self.est_vide():
            return "Erreur: La file est vide"
        else:
            return self.base_de_donnee[self.index_tete]
    
    def close(self):
        """Méthode qui renvoie les modifications qu'on a fait aux données dans le fichier originale."""
        with open(self.filename, "w") as f:
            json.dump(self.base_de_donnee, f, indent= 2)
