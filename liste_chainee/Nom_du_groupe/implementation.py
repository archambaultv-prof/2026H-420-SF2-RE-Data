class Knots:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer: 'Knots' = pointer


class Chained_List:
    def __init__(self, first: Knots = None):
        self.first = first

    def first_add(self, knots: Knots):
        knots.pointer = self.first
        self.first = knots

    def last_add(self, knots: Knots):
        if self.first is None:
            self.first = knots
            knots.pointer = None
            return
        current = self.first
        while current.pointer is not None:
            current = current.pointer
        current.pointer = knots
        knots.pointer = None

    def is_first(self, knots: Knots):
        return self.first is knots

    def is_last(self, knots: Knots):
        if self.first is None:
            return False
        current = self.first
        while current.pointer is not None:
            current = current.pointer
        return current is knots

    def pointer_first(self, knots_in_chained_list: Knots):
        if self.first is knots_in_chained_list:
            return
        prev = None
        current = self.first
        while current is not None and current is not knots_in_chained_list:
            prev = current
            current = current.pointer
        if current is None:
            raise ValueError("node not in list")
        prev.pointer = current.pointer
        current.pointer = self.first
        self.first = current

    def pointer_last(self, knots_in_chained_list: Knots):
        if self.first is None:
            raise ValueError("empty list")
        prev = None
        current = self.first
        while current is not None and current is not knots_in_chained_list:
            prev = current
            current = current.pointer
        if current is None:
            raise ValueError("node not in list")
        if current.pointer is None:
            return
        if prev is None:
            self.first = current.pointer
        else:
            prev.pointer = current.pointer
        tail = self.first
        while tail.pointer is not None:
            tail = tail.pointer
        tail.pointer = current
        current.pointer = None

    def lenght(self):
        count = 0
        current = self.first
        while current is not None:
            count += 1
            current = current.pointer
        return count
    length = lenght

    def remove(self, value):
        if self.first is None:
            raise IndexError("remove from empty list")
        prev = None
        current = self.first
        while current is not None:
            if current.value == value:
                if prev == None:
                    self.first = None
                else:
                    prev.pointer = current.pointer
                    del current
            prev = current
            current = current.pointer

    def search(self, search_value):
        current = self.first
        while current is not None:
            if current.value == search_value:
                return True
            current = current.pointer
        return False