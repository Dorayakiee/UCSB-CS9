#pytests for Queue

from Queue import Queue

def test_insertIntoQueue():
    q = Queue()
    assert q.isEmpty() == True
    assert q.size() == 0

    q.enqueue("Customer 1")
    q.enqueue("Customer 2")
    assert q.isEmpty() == False
    assert q.size() == 2

def test_removeFromQueue():
    q = Queue()
    q.enqueue("Customer 1")
    q.enqueue("Customer 2")

    assert q.dequeue() == "Customer 1"
    assert q.isEmpty() == False
    assert q.size() == 1

    assert q.dequeue() == "Customer 2"
    assert q.isEmpty() == True
    assert q.size() == 0