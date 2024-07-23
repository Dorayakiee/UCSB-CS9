from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car_str():
    c = Car("Honda", "CRV", 2007, 8000)
    assert str(c) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"
    c2 = Car("Mazda", "CX-5", 2015, 12000)
    assert str(c2) == "Make: MAZDA, Model: CX-5, Year: 2015, Price: $12000"
    c3 = Car("Toyota", "Camry", 2020, 22000)
    assert str(c3) == "Make: TOYOTA, Model: CAMRY, Year: 2020, Price: $22000"

def test_InOrder_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Honda", "Civic", 2019, 20000)
    assert bst.inOrder() == ""
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: HONDA, Model: CIVIC, Year: 2019, Price: $20000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

def test_inOrder():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porsche", "911", 2023, 120000)
    car6 = Car("Chevrolet", "Impala", 2010, 9000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.inOrder() == \
"""\
Make: BUGATTI, Model: VEYRON, Year: 2011, Price: $2000000
Make: CHEVROLET, Model: IMPALA, Year: 2010, Price: $9000
Make: DODGE, Model: DURANGO, Year: 2023, Price: $50000
Make: GMC, Model: YUKON, Year: 1996, Price: $7000
Make: GMC, Model: YUKON, Year: 2023, Price: $40000
Make: PORSCHE, Model: 911, Year: 2023, Price: $120000
"""

def test_preOrder_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    assert bst.inOrder() == ""
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""


def test_preOrder():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porsche", "911", 2023, 120000)
    car6 = Car("Chevrolet", "Corvette", 2015, 45000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.preOrder() == \
"""\
Make: GMC, Model: YUKON, Year: 1996, Price: $7000
Make: GMC, Model: YUKON, Year: 2023, Price: $40000
Make: DODGE, Model: DURANGO, Year: 2023, Price: $50000
Make: BUGATTI, Model: VEYRON, Year: 2011, Price: $2000000
Make: CHEVROLET, Model: CORVETTE, Year: 2015, Price: $45000
Make: PORSCHE, Model: 911, Year: 2023, Price: $120000
"""

def test_postOrder_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    assert bst.inOrder() == ""
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""

def test_postOrder():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porche", "911", 2023, 120000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.postOrder() == \
"""\
Make: BUGATTI, Model: VEYRON, Year: 2011, Price: $2000000
Make: DODGE, Model: DURANGO, Year: 2023, Price: $50000
Make: PORCHE, Model: 911, Year: 2023, Price: $120000
Make: GMC, Model: YUKON, Year: 1996, Price: $7000
Make: GMC, Model: YUKON, Year: 2023, Price: $40000
"""

def test_doesCarExist():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Chevrolet", "Malibu", 2018, 16000)
    bst.addCar(car1)
    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car2) == False
    bst.addCar(car2)
    assert bst.doesCarExist(car2) == True
    assert bst.doesCarExist(car3) == False
    bst.addCar(car3)
    assert bst.doesCarExist(car3) == True

def test_getBestCar_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Audi", "A4", 2017, 22000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Audi", "A4") == car6
    assert bst.getBestCar("Honda", "Accord") == None

def test_getBestCar():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porsche", "911", 2023, 120000)
    car6 = Car("Chevrolet", "Corvette", 2015, 45000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.getBestCar("GMC", "Yukon") == car2
    assert bst.getBestCar("Bugatti", "Veyron") == car4
    assert bst.getBestCar("Chevrolet", "Corvette") == car6
    assert bst.getBestCar("Candy", "Crush") == None

def test_getWorstCar_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Audi", "A4", 2017, 22000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getWorstCar("Audi", "A4") == car6
    assert bst.getWorstCar("Honda", "Accord") == None

def test_getWorstCar():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porsche", "911", 2023, 120000)
    car6 = Car("Chevrolet", "Impala", 2010, 9000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.getWorstCar("GMC", "Yukon") == car1
    assert bst.getWorstCar("Porsche", "911") == car5
    assert bst.getWorstCar("Chevrolet", "Impala") == car6
    assert bst.getWorstCar("Candy", "Crush") == None

def test_getTotalInventoryPrice_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Audi", "A4", 2017, 22000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.getTotalInventoryPrice() == 180000

def test_getTotalInventoryPrice():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porsche", "911", 2023, 120000)
    car6 = Car("Chevrolet", "Corvette", 2015, 45000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    assert bst.getTotalInventoryPrice() == 2262000
