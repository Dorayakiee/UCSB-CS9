from CustomPizza import CustomPizza
from Pizza import Pizza
from SpecialtyPizza import SpecialtyPizza


class PizzaOrder:
    def __init__(self, time):
        self.time = time
        self.order = []

    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.order.append(pizza)

    def getOrderDescription(self):
        pri = 0.0
        res = "******\n"
        res += f"Order Time: {self.time}\n"
        for pizza in self.order:
            pri += pizza.price
            res += pizza.getPizzaDetails()
            res += "\n----\n"
        res += f"TOTAL ORDER PRICE: ${pri:.2f}\n"
        res += "******\n"
        return res
        
    