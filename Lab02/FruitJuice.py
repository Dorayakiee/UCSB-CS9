from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits
    def getInfo(self):
        s = "/".join(self.fruits) + " Juice"
        return f"{s}, {super().getInfo()}"
    
# juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
# print(juice.getInfo()) 
