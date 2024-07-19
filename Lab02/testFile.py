from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

class TestBeverage:
    def test_init(self):
        b1 = Beverage(44, 18)
        b2 = Beverage(16, 19.98)
        assert b1.ounces == 44
        assert b1.price == 18.00
        assert b2.ounces == 16
        assert b2.price == 19.98

    def test_getOunces(self):
        b1 = Beverage(44, 18)
        b2 = Beverage(16, 19.98)
        assert b1.getOunces() == 44
        assert b2.getOunces() == 16

    def test_getPrice(self):
        b1 = Beverage(44, 18)
        b2 = Beverage(16, 19.98)
        assert b1.getPrice() == 18.00
        assert b2.getPrice() == 19.98

    def test_updateSize(self):
        b1 = Beverage(44, 18)
        b2 = Beverage(16, 19.98)
        b1.updateOunces(20)
        assert b1.ounces == 20
        b2.updateOunces(114514)
        assert b2.ounces == 114514

    def test_updatePrice(self):
        b1 = Beverage(44, 18)
        b2 = Beverage(16, 19.98)
        b1.updatePrice(11.44)
        assert b1.price == 11.44
        b2.updatePrice(20)
        assert b2.price == 20

    def test_getInfo(self):
        b1 = Beverage(44, 18)
        b2 = Beverage(16, 19.98)
        assert b1.getInfo() == "44 oz, $18.00"
        assert b2.getInfo() == "16 oz, $19.98"


class TestFruitJuice:
    def test_init(self):
        f1 = FruitJuice(16, 22.5, ["Apple","Banana"])
        assert f1.price == 22.5
        assert f1.fruits == ["Apple","Banana"]
        assert f1.ounces == 16

    def test_getInfo(self):
        f1 = FruitJuice(16, 22.5, ["Apple","Banana","Peach"])
        assert f1.getInfo() == "Apple/Banana/Peach Juice, 16 oz, $22.50"


class TestCoffee:
    def test_init(self):
        c1 = Coffee(16, 29.8, "Martini")
        assert c1.ounces == 16
        assert c1.price == 29.8
        assert c1.style == "Martini"

    def test_getInfo(self):
        c1 = Coffee(16, 29.8, "Martini")
        assert c1.getInfo() == "Martini Coffee, 16 oz, $29.80"

class TestDrinkOrder:
    def test_init(self):
        o1 = DrinkOrder()
        assert type(o1.drinks) == list
    def test_addBeverage(self):
        o1 = DrinkOrder()
        f1 = FruitJuice(16, 22.5, ["Apple","Banana"])
        c1 = Coffee(16, 29.8, "Martini")
        o1.addBeverage(f1)
        o1.addBeverage(c1)
        assert o1.drinks == [f1, c1]

    def test_getTotalOrder(self):
        o1 = DrinkOrder()
        f1 = FruitJuice(16, 22.5, ["Apple","Banana"])
        c1 = Coffee(16, 29.8, "Martini")
        o1.addBeverage(f1)
        o1.addBeverage(c1)
        assert o1.getTotalOrder() == "Order Items:\n* Apple/Banana Juice, 16 oz, $22.50\n* Martini Coffee, 16 oz, $29.80\nTotal Price: $52.30"