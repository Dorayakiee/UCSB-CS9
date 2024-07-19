# LinkedListTest

from LinkedList import LinkedList, Node

def test_NodeCreation():
    n = Node(20)
    assert n.getData() == 20
    assert n.getNext() == None

def test_NodeSetData():
    n = Node(20)
    n.setData(200)
    assert n.getData() == 200

def test_NodeSetNext():
    n = Node(20)
    n2 = Node(10)
    n.setNext(n2)
    assert n.getNext() == n2

def test_createList():
    ll = LinkedList()
    assert ll.isEmpty() == True

def test_addNodesToList():
    ll = LinkedList()
    assert ll.isEmpty() == True

    ll.addToFront(10)
    ll.addToFront("nodenodenode")
    ll.addToFront(True)

    assert ll.isEmpty() == False
    assert ll.length() == 3
    assert ll.search(10) == True
    assert ll.search(True) == True
    assert ll.search("CS9") == False

def test_removeNodesFromList():
    ll = LinkedList()
    assert ll.isEmpty() == True

    ll.addToFront(10)
    ll.addToFront("nodenodenode")
    ll.addToFront(True)

    assert ll.length() == 3
    assert ll.search("nodenodenode") == True
    ll.remove("nodenodenode")
    assert ll.search("nodenodenode") == False
    assert ll.length() == 2

    assert ll.search(True) == True
    ll.remove(True)
    assert ll.search(True) == False
    assert ll.length() == 1

    assert ll.search(10) == True
    ll.remove(10)
    assert ll.search(10) == False
    assert ll.length() == 0
    assert ll.isEmpty() == True

def test_insertIntoOrderedList():
    ll = LinkedList()
    ll.add(35)
    ll.add(50)
    ll.add(10)
    ll.add(40)
    ll.add(20)
    ll.add(30)

    assert ll.getList() == "10 20 30 35 40 50"

    ll.add(5)
    assert ll.getList() == "5 10 20 30 35 40 50"

    ll.add(60)
    assert ll.getList() == "5 10 20 30 35 40 50 60"