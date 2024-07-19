#from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

# class DrinkOrder:
#     def __init__(self):
#         self.drinks = list()
#     def addBeverage(self, beverage):
#         self.drinks.append(beverage)

#     def getTotalOrder(self):
#         s = "Order Items:"
#         s += "\n"
#         count = 0
#         for i in self.drinks:
#             s += "* "
#             s += i.getInfo()
#             s += "\n"
#             count += i.price
#         s += f"Total Price: ${count}"
#         return s
class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        if not self.drinks:
            return "Order Items:\nTotal Price: $0.00"

        s = "Order Items:\n"
        total_price = 0.0
        for drink in self.drinks:
            s += f"* {drink.getInfo()}\n"
            total_price += drink.price
        s += f"Total Price: ${total_price:.2f}"
        return s
    
# c1 = Coffee(8, 3.0, "Espresso")
# juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
# order = DrinkOrder()
# order.addBeverage(c1)
# order.addBeverage(juice)
# print(order.getTotalOrder())
# o1 = DrinkOrder()
# f1 = FruitJuice(16, 22.5, ["Apple","Banana"])
# b1 = Beverage(44, 18)
# c1 = Coffee(16, 29.8, "Martini")
# o1.addBeverage(f1)
# o1.addBeverage(c1)
# print(o1.getTotalOrder())