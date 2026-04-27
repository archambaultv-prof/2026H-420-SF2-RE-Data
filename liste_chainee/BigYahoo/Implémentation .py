class Noeud:
    
 
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None
 
 
class ListeChainee:
    
 
    def __init__(self):
        self.tete = None
 
 
    def inserer_en_tete(self, valeur):
        
        nouveau = Noeud(valeur)
        nouveau.suivant = self.tete
        self.tete = nouveau
 
    def inserer_en_queue(self, valeur):
       
        nouveau = Noeud(valeur)
        if self.tete is None:
            self.tete = nouveau
            return
        courant = self.tete
        while courant.suivant is not None:
            courant = courant.suivant
        courant.suivant = nouveau
 
    
    def supprimer(self, valeur):
        
        if self.tete is None:
            return False
 
        
        if self.tete.valeur == valeur:
            self.tete = self.tete.suivant
            return True
 
        courant = self.tete
        while courant.suivant is not None:
            if courant.suivant.valeur == valeur:
                courant.suivant = courant.suivant.suivant
                return True
            courant = courant.suivant
 
        return False  
 
     #
 
    def rechercher(self, valeur):
       
        courant = self.tete
        while courant is not None:
            if courant.valeur == valeur:
                return True
            courant = courant.suivant
        return False
 
    
    def taille(self):
        
        compteur = 0
        courant = self.tete
        while courant is not None:
            compteur += 1
            courant = courant.suivant
        return compteur
 
    def afficher(self):
       
        elements = []
        courant = self.tete
        while courant is not None:
            elements.append(str(courant.valeur))
            courant = courant.suivant
        print(" -> ".join(elements) + " -> None")
 
    def est_vide(self):
        
        return self.tete is None
 
 
 
if __name__ == "__main__":
    
    liste = ListeChainee()
 
    
    liste.inserer_en_queue(10)
    liste.inserer_en_queue(20)
    liste.inserer_en_queue(30)
    liste.inserer_en_tete(5)
   
    liste.afficher()                          
 
    
    print(f"Taille : {liste.taille()}")       
 
    
    print(f"Recherche 20 : {liste.rechercher(20)}")   
    print(f"Recherche 99 : {liste.rechercher(99)}")   
 
    
    liste.supprimer(10)

    liste.afficher()                         
    
    print(f"Est vide : {liste.est_vide()}")   