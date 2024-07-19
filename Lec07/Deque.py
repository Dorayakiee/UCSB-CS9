# Deque

class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    # Big-O analysis
    # O(1)
    def addFront(self, item):
        self.items.append(item)
    
    # Big-O analysis
    # O(n)
    def addRear(self, item):
        self.items.insert(0, item)
    
    # Big-O analysis
    # O(1)
    def removeFront(self):
        return self.items.pop()
    
    # Big-O analysis
    # O(n)
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)