from Pizza import Pizza

pricemap = {"S":8.00, "M":10.00, "L":12.00}
toppingprice = {"S":0.50, "M":0.75, "L":1.00}

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        self.price = pricemap[size]

    def addTopping(self, topping):
        self.toppings.append(topping)
        self.price += toppingprice[self.size]

    def getPizzaDetails(self):
        res = f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\n"
        for i in self.toppings:
            res += f"\t+ {i}\n"
        res += f"Price: ${self.price:.2f}\n"
        return res

