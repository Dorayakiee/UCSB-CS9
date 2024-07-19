# Stack.py

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    # Big-O analysis
    # O(1) - constant time
    def push(self, item):
        self.items.append(item)
    
    # Big-O analysis
    # Also O(1) - constant time
    def pop(self):
        return self.items.pop()
    
    # Big-O analysis
    # Also O(1) - constant time
    def peek(self):
        return self.items[len(self.items) - 1]
        #return self.items[-1]
    
    def size(self):
        return len(self.items)