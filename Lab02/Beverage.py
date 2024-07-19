class Beverage:
    def __init__(self, ounces = None, price = None):
        self.ounces = ounces
        self.price = price
    def updateOunces(self, newOunces):
        self.ounces = newOunces
    def updatePrice(self, newPrice):
        self.price = newPrice
    def getOunces(self):
        #return f"{self.ounces} oz"
        return self.ounces
    def getPrice(self):
        #return f"${self.price:.2f}"
        return self.price
    def getInfo(self):
       # return self.getOunces() + ", " + self.getPrice()
        return f"{self.ounces} oz, ${self.price:.2f}"
    

# b1 = Beverage(44, 18)
# b2 = Beverage(16, 19.98)
# print(b1.getInfo())
# print(b2.getInfo())
# print(b1.getOunces())
# print(b1.getPrice())
# print(b2.getPrice())
# print(b2.getOunces())

# b1 = Beverage(16, 20.5)
# print(b1.getInfo())
# #assert b1.getInfo() == "16 oz, $20.50"