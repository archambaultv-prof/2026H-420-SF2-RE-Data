# liste chaînées
structure de données composée de d'une donnée et d'un pointeur vers le prochain élément comme une chaîne.

# Opérations princpales

## Traversal (parcours)
- parcourir tous les noeuds un par un du début jusqu'à la fin de la liste chianée. 

## Insertion (Insert)
- ajouter un nouveau noeud à la liste chainée, au début, à la fin, ou au milieu en modifiant les liens a autour du nouveau noeud.

## Supression (Delete)
- supprimer un noeud de la liste en ajustant les liens entre les autres noeuds pour maintenir la structure de la liste chainée.

## Chercher (find) 
- chercher un noeud contenant une valeure spécifique en parcourant la liste 

# Avantages
- Insertion et suppression faciles : pas besoin de déplacer les autres éléments, on modifie juste les liens
- Taille dynamique : peut grandir ou rétrécir facilement sans limite fixe
- Pas besoin de mémoire contiguë : les éléments peuvent être stockés n’importe où en mémoire

# Désavantages 
- Accès lent aux éléments : il faut parcourir la liste depuis le début (pas d’accès direct comme un tableau)
- Utilise plus de mémoire : chaque nœud stocke une référence en plus de la donnée
- Manipulation plus complexe : gestion des pointeurs peut être plus difficile et source d’erreurs

# Exemples d'utilisation

``` python
class Noeud :
    def __init__(self, data):
        self.data = data  
        self.next = None      


class ListeChainee :
    def __init__(self):
        self.head = None


    def insert_debut(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_fin(self, data):
        new_node = Noeud(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_position(self, data, position):
        new_node = Noeud(data)

        if position == 0:
            self.insert_debut(data)
            return

        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Position invalide")
            return

        new_node.next = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        
        if current is None:
            return
        
        if current.data == key:
            self.head = current.next
            return
            
        prev = None
        
        while current and current.data != key:
            prev = current
            current = current.next
            
        if current is None:
            return
            
        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


ll = ListeChainee()
ll.insert_debut(5)
ll.insert_fin(8)
ll.insert_fin(12)

print("Avant insertion :")
ll.display()

ll.insert_position(10, 2)

print("Après insertion au milieu :")
ll.display()
```

