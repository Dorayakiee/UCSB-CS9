class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next = newNext

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def addToFront(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def length(self):
        current_node = self.head
        count = 0
        while current_node != None:
            count = count + 1
            current_node = current_node.getNext()
        return count

    def search(self, data):
        current_node = self.head
        found = False
        while current_node != None and not found:
            if current_node.getData() == data:
                found = True
            else:
                current_node = current_node.getNext()
        return found

    def remove(self, data):
        current = self.head

        if current == None:
            return

        previous = None
        found = False
        
        while not found:  # Find the element
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
            
        # Case 1: remove 1st element
        if found == True and previous == None:
            self.head = current.getNext()
        
        # Case 2: remove not 1st element
        if found == True and previous != None:
            previous.setNext(current.getNext())
    
    # Assuming an Ordered Linked List
    def add(self, data):
        current = self.head
        previous = None

        # find the correct position in the list to add
        while current != None:
            if current.getData() > data:
                break
            else:
                previous = current
                current = current.getNext()
        
        # create Node with data to add
        newNode = Node(data)

        # Case 1: insert at the front of the list
        if previous == None:
            newNode.setNext(self.head)
            self.head = newNode
        else: # Case 2: insert not at the front of the list
            newNode.setNext(current)
            previous.setNext(newNode)
    
    # Method to get the items from front to back
    def getList(self):
        current = self.head
        output = ""
        while current != None:
            output += str(current.getData()) + " "
            current = current.getNext()
        output = output[:len(output) - 1] # remove trailing space
        return output
