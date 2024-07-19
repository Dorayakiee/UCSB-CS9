

class Pizza:
    def __init__(self, size ,price = 0.0):
        self.price = price
        self.size = size

    def getPrice(self):
        return self.price
    
    def getSize(self):
        return self.size
    
    def setPrice(self, price):
        self.price = price
        

    def setSize(self,size):
        self.size = size

    