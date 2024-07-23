from Car import Car


class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getParent(self):
        if not self.parent:
            return None
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        if not self.left:
            return None
        return self.left
    
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        if not self.right: 
            return None
        return self.right
    
    def setRight(self, right):
        self.right = right 


    def __str__(self):
        ret = []
        for car in self.cars:
            ret.append(str(car))
            ret.append('\n')
        return "".join(ret)



# car1 = Car("Dodge", "dart", 2015, 6000)
# car2 = Car("dodge", "DaRt", 2003, 5000)
# carNode = CarInventoryNode(car1)
# carNode.cars.append(car2)
# print(carNode)