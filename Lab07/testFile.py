from CustomPizza import CustomPizza
from Pizza import Pizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue, QueueEmptyException

##Pizza

def test_Pizza():
    p1 = Pizza("S", 114.51)
    p2 = Pizza("M", 1919.81)
    assert p1.getPrice() == 114.51
    assert p1.getSize() == "S"
    assert p2.getSize() == "M"
    p2.setPrice(191.81)
    assert p2.getPrice() == 191.81


###CustomPizza

def test_custompizza_getpizzadetails():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    cp2 = CustomPizza("L")
    cp2.addTopping("extra cheese")
    cp2.addTopping("sausage")

    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"

    cp2 = CustomPizza("M")
    cp2.addTopping("anchovies")
    cp2.addTopping("jelly beans")
    cp2.addTopping("bananas")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ anchovies\n\
\t+ jelly beans\n\
\t+ bananas\n\
Price: $12.25\n"
    cp2.addTopping("mushrooms")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ anchovies\n\
\t+ jelly beans\n\
\t+ bananas\n\
\t+ mushrooms\n\
Price: $13.00\n"

###SpecialPizza

def test_specia_getdetails():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    sp2 = SpecialtyPizza("M", "Meat")
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: Meat\n\
Price: $14.00\n"
    sp3 = SpecialtyPizza("L", "Calzo")
    assert sp3.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: Calzo\n\
Price: $16.00\n"


###PizzaOrder

def test_pizzaorder_getorder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(121212) 
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 121212\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"
    cp1 = CustomPizza("S")
    cp1.addTopping("double cheese")
    cp1.addTopping("tomatoes")
    sp1 = SpecialtyPizza("S", "Cheesey")
    order = PizzaOrder(240001) 
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 240001\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ double cheese\n\
\t+ tomatoes\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Cheesey\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

    cp2 = CustomPizza("L")
    cp2.addTopping("chicken")
    cp2.addTopping("onions")
    sp2 = SpecialtyPizza("M", "The UFO")
    order.addPizza(cp2)
    order.addPizza(sp2)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 240001\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ double cheese\n\
\t+ tomatoes\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Cheesey\n\
Price: $12.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ chicken\n\
\t+ onions\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: The UFO\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $49.00\n\
******\n"   


###OrderQueue


def test_OrderQueue_processnextorder():
    order1 = PizzaOrder(83000) 
    cp1 = CustomPizza("M")
    order1.addPizza(cp1)
    order2 = PizzaOrder(140000) 
    cp2 = CustomPizza("L")
    order2.addPizza(cp2)
    order3 = PizzaOrder(114521) 
    sp1 = SpecialtyPizza("L", "Garden")
    order3.addPizza(sp1)
    order4 = PizzaOrder(74556) 
    sp2 = SpecialtyPizza("M", "Carnivore")
    order4.addPizza(sp2)
    order5 = PizzaOrder(134500) 
    cp3 = CustomPizza("M")
    cp3.addTopping("mushrooms")
    order5.addPizza(cp3)

    orderQueue = OrderQueue()
    orderQueue.addOrder(order1)
    orderQueue.addOrder(order2)
    orderQueue.addOrder(order3)
    orderQueue.addOrder(order4)
    orderQueue.addOrder(order5)

    assert orderQueue.processNextOrder() == \
"******\n\
Order Time: 74556\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Carnivore\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $14.00\n\
******\n"
    a = OrderQueue()
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order1 = PizzaOrder(121212)
    order1.addPizza(cp1)
    order1.addPizza(sp1)
    order2 = PizzaOrder(131412)
    order2.addPizza(cp1)
    order3 = PizzaOrder(225659)
    order3.addPizza(sp1)
    a.addOrder(order3)
    a.addOrder(order2)
    a.addOrder(order1)
    assert a.heaplist[1].getTime() == 121212
    assert a.processNextOrder() == "******\n\
Order Time: 121212\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"
    assert a.heaplist[1].time == 131412
    order4 = PizzaOrder(111111)
    order4.addPizza(sp1)
    a.addOrder(order4)
    assert a.heaplist[1].getTime() == 111111

    
    
    