class Node:
    def __init__(self, data):
        self.data = data      # valeur
        self.next = None      # pointeur vers le suivant


class LinkedList:
    def __init__(self):
        self.head = None

    # Ajouter au début
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Ajouter à la fin
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Ajouter au milieu (à une position)
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            self.insert_at_head(data)
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


# 🔧 Exemple d'utilisation
ll = LinkedList()
ll.insert_at_head(5)
ll.insert_at_tail(8)
ll.insert_at_tail(12)

print("Avant insertion :")
ll.display()

ll.insert_at_position(10, 2)

print("Après insertion au milieu :")
ll.display()