#Queue.py

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    # Big-O analysis
    # O(n)
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # Big-O analysis
    # O(1) -- constant time
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
