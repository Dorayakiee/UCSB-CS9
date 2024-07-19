# pytest for Stack
from Stack import Stack

def test_insertIntoStack():
    s = Stack()
    s.push("There")
    s.push("Hi")
    assert s.size() == 2
    assert s.peek() == "Hi"
    assert s.isEmpty() == False

def test_deleteFromStack():
    s = Stack()
    s.push("There")
    s.push("Hi")
    x = s.pop()
    assert x == "Hi"

    assert s.peek() == "There"
    assert s.size() == 1
    assert s.isEmpty() == False
    
    y = s.pop()
    assert y == "There"
    assert s.size() == 0
    assert s.isEmpty() == True