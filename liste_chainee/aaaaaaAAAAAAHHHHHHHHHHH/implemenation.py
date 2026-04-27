class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def insert(self, data, index):
        if index < 0:
            raise IndexError("InvalidIndex")
        if index == 0:
            temp = LinkedList(self.data)
            if self.next is not None:
                temp.add(self.next)
            self.data = data
            self.next = temp
        elif self.next is None:
            raise IndexError("OutofRange")
        else:
            self.next.insert(data, index-1)

    def add(self, element):
        if self.next is None:
            self.next = LinkedList(element)
        else:
            self.next.add(element)
    
    def find(self, index):
        if index < 0:
            raise IndexError("InvalidIndex")
        if index == 0:
            return self.data
        elif self.next is None:
            raise IndexError("OutofRange")
        else:
            return self.next.find(index-1)
    
    def index(self, data):
        if self.data == data:
            return 0
        elif self.next is None:
            raise FileNotFoundError("NotinList")
        else:
            return self.next.index(data)+1
    
    def present(self, data):
        if self.data == data:
            return True
        elif self.next is None:
            return False
        else:
            return self.next.present(data)

    def remove(self, index):
        if index == 0:
            if self.next is not None:
                self.data = self.next.data
                self.next = self.next.next
            else:
                self.data = None
                self.next = None
        elif self.next is None:
            raise IndexError("OutofRange")
        else:
            self.next.remove(index-1)
            if self.next.data is None:
                self.next = None
    
    def __str__(self):
        return f"[{self.data}{f", {self.next}".replace("[", "").replace("]", "") if self.next is not None else ""}]"




class LinkedList2:
    def __init__(self, data):
        self.data = [data, None]

    def add(self, data):
        ls = self.data
        while ls[1] is not None:
            ls = ls[1]
        ls[1] = [data, None]
    
    def insert(self, data, index):
        ls = self.data
        while index > 0:
            ls = ls[1]
        if ls is None:
            self.add(data)
        else:
            ls[1] = [data, ls[1]]
    
    def find(self, index):
        ls = self.data
        while index > 0:
            ls = ls[1]
            index -= 1
        return ls[0]
    
    def index(self, data):
        ls = self.data
        index = 0
        while ls is not None:
            if ls[0] == data:
                return index
            else:
                ls = ls[1]
                index += 1
        raise FileNotFoundError("NotInList")
        
    def present(self, data):
        ls = self.data
        while ls is not None:
            if ls[0] == data:
                return True
            else:
                ls = ls[1]
        return False
    
    def remove(self, index):
        if index == 0 and self.data[1] is not None:
            self.data = self.data[1]
        elif index == 0:
            self.data = [None, None]
        else:
            ls = self.data
            i = index
            while index > 1:
                ls = ls[1]
                i -= 1
            if ls[1][1] is not None:
                ls[1] = ls[1][1]
            else:
                ls[1] = None
        
    def __str__(self):
        return f"{self.data}"