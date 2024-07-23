from Car import Car
from CarInventoryNode import CarInventoryNode


class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0

    def addCar(self, car):
        if self.root:
            self._addCar(car, self.root)
        else :
            self.root = CarInventoryNode(car)


    def _addCar(self, car, node):
        if car.make == node.make and car.model == node.model:
            node.cars.append(car)
        elif car < node.cars[0]:
            if node.left:
                self._addCar(car,node.left)
            else:
                node.setLeft(CarInventoryNode(car))

        elif car > node.cars[0]:
            if node.right:
                self._addCar(car,node.right)
            else:
                node.setRight(CarInventoryNode(car))

    # def addCar(self, car):
    #     if self.root:
    #         print(f"Adding {car} to the tree.")
    #         self._addCar(car, self.root)
    #     else:
    #         self.root = CarInventoryNode(car)
    #         print(f"Root is now {car}")

    # def _addCar(self, car, node):
    #     if car.make == node.make and car.model == node.model:
    #         node.cars.append(car)
    #         print(f"Appended {car} to node {node}")
    #     elif car < node.cars[0]:
    #         if node.left:
    #             self._addCar(car, node.left)
    #         else:
    #             node.setLeft(CarInventoryNode(car))
    #             print(f"Set left of {node} to {car}")
    #     else:
    #         if node.right:
    #             self._addCar(car, node.right)
    #         else:
    #             node.setRight(CarInventoryNode(car))
    #             print(f"Set right of {node} to {car}")

    def doesCarExist(self, car):
        found = False
        
        if not self.root:
            return False
        node = self.root
        while not found:
            if car.model == node.model and car.make == node.make:
                for i in node.cars:
                    if i == car:
                        return True
                return False
                    
            elif car.make < node.make or car.make == node.make and car.model < node.model:
                if not node.left:
                    return False
                else:
                    node = node.left
            elif car.make > node.make or car.make == node.make and car.model > node.model:
                if not node.right:
                    return False
                else:
                    node = node.right


    def inOrder(self):
        return self._inOrder(self.root)
    
    def _inOrder(self,node):
        ret = ""
        if node != None:
            ret += self._inOrder(node.left)
            for car in node.cars:
                ret += str(car) + "\n"
            ret += self._inOrder(node.right)
        return ret
    
    def preOrder(self):
        return self._preOrder(self.root)
    
    def _preOrder(self, node):
        ret = ""
        if node != None:
            for car in node.cars:
                ret += str(car) + "\n"
            ret += self._preOrder(node.left)
            ret += self._preOrder(node.right)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)
    
    def _postOrder(self, node):
        ret = ""
        if node != None:
            ret += self._postOrder(node.left)
            ret += self._postOrder(node.right)
            for car in node.cars:
                ret += str(car) + "\n"
        return ret
    
    def getBestCar(self, make, model):
        make = make.upper()
        model = model.upper()
        if not self.root:
            return None
        else:
            node = self.root
            while True:
                if make == node.make and model == node.model:
                   # print("node found\n")
                    ret = Car(make,model,0,0)
                    for i in node.cars:
                        if i > ret:
                            ret = i
                    return ret
                
                elif make > node.make or make == node.make and model > node.model:
                    if not node.right:
                        #print("right error\n")
                        return None
                    else:
                        node = node.right
                        #print("itr node right\n")
                
                elif make < node.make or make == node.make and model < node.model:
                    if not node.left:
                        #print("left error\n")
                        return None
                    else:
                        node = node.left
                       # print("itr node left\n")


    def getWorstCar(self, make, model):
        make = make.upper()
        model = model.upper()
        if not self.root:
            return None
        else:
            node = self.root
            while True:
                if make == node.make and model == node.model:
                    ret = node.cars[0]
                    for i in node.cars:
                        if i < ret:
                            ret = i
                    return ret
                
                elif make > node.make or make == node.make and model > node.model:
                    if not node.right:
                        return None
                    else:
                        node = node.right
                
                elif make < node.make or make == node.make and model < node.model:
                    if not node.left:
                        return None
                    else:
                        node = node.left


    def getTotalInventoryPrice(self):
        if not self.root:
            return 0
        else:
            ans = 0
            for i in self.root.cars:
                ans += i.price
            ans += self._getPrice(self.root.left)
            ans += self._getPrice(self.root.right)
        return ans
            

    def _getPrice(self,node):
        if not node:
            return 0
        ans = 0
        for i in node.cars:
            ans += i.price
        ans += self._getPrice(node.left)
        ans += self._getPrice(node.right)
        return ans
    
# bst = CarInventory()

# car1 = Car("Nissan", "Leaf", 2018, 18000)
# car2 = Car("Tesla", "Model3", 2018, 50000)
# car3 = Car("Mercedes", "Sprinter", 2022, 40000)
# car4 = Car("Mercedes", "Sprinter", 2014, 25000)
# car5 = Car("Ford", "Ranger", 2021, 25000)

# bst.addCar(car1)
# bst.addCar(car2)
# bst.addCar(car3)
# bst.addCar(car4)
# bst.addCar(car5)

# print(bst.getBestCar("Nissan", "Leaf"))
