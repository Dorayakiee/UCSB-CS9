from Pizza import Pizza

pricemap = {"S":12.00, "M":14.00, "L":16.00}
toppingprice = {"S":0.50, "M":0.75, "L":1.00}

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        self.price = pricemap[size]

    def getPizzaDetails(self):
        res = f"SPECIALTY PIZZA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n"
        return res