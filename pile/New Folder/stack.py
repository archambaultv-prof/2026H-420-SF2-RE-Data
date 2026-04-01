class Stack:
    def __init__(self):
        self.stack = [None] * 50
        self.current_index = 0
    
    def push(self, data):
        if self.current_index == len(self.stack):
            self.stack += [None] * int(len(self.stack)*2**0.5)
        self.stack[self.current_index] = data
        self.current_index += 1
    
    def pull(self):
        if self.current_index == 0:
            return None
        elif self.current_index < int(len(self.stack)/2**0.5) and int(len(self.stack)/2**0.5) >= 50:
            self.stack = self.stack[:int(len(self.stack)/2**0.5)]
        self.current_index -= 1
        return self.stack[self.current_index]
    
if __name__ == "__main__":
    stack1 = Stack()
    for i in range(100):
        stack1.push(i)
    for i in range(100):
        print(stack1.pull())
        print(len(stack1.stack))