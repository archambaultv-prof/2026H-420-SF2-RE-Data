class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        node = Node(value)
        self.children.append(node)
        return node

    def find_child(self, value):
        for index, child in enumerate(self.children):
            if child.value == value:
                return index
        return None

    def remove_child(self, value):
        index = self.find_child(value)
        if index is not None:
            del self.children[index]

arbre = Node("root")
child = arbre.add_child("child1")

ls = [1,2,3]
next_item = [4]
ls.extend(next_item)