# pytest Deque

from Deque import Deque

def test_Deque():
    d = Deque()
    assert d.isEmpty() == True
    assert d.size() == 0

    d.addFront(10)
    d.addFront(20)
    d.addRear(30)
    d.addRear(40)

    assert d.isEmpty() == False
    assert d.size() == 4

    assert d.removeFront() == 20
    assert d.removeRear() == 40
    assert d.isEmpty() == False
    assert d.size() == 2

    # [ 30 10 ]
    assert d.removeRear() == 30
    # [ 10 ]
    assert d.removeRear() == 10
    assert d.isEmpty() == True
    assert d.size() == 0