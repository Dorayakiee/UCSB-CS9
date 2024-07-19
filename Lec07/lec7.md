% Lecture 7
% Wed Jul 10, 2024

Today:

* Stacks
* Queues
* Deques
* (Maybe Linked Lists)

# Stacks

* We've discussed stack at a high level (their property).
* Let's go through an implementation using Python lists (implementation in the textbook).
* See `Stack.py` and `StackTest.py`.

```
push---+  ---> pop
    |   | |
    |   v |
    |     |
    |-----|
peek|>    |
    |-----|


[ bottom , , , , , , , top ]
   0                   n-1
```

# Queues

* A queue is a linear data structure that has the First In, First Out (FIFO) property.
* Analogy: Think about standing in line (no cutting!).
* Similar to a Stack, we can implement a Queue using a Python list.
* See `Queue.py` and `QueueTest.py`.

```
Queue

enqueue --> [  |  |  |  |  |  |  ] --> dequeue
             0                 n-1

First In, First Out (FIFO)

```

# Deque

* Pronounced "Deck".
* A deque is a linear data structure that is more flexible than a stack or a queue.
    - Also known as a "double-ended queue".
    - A deque allows us to insert and remove from both ends.
    - Unlike a stack where we can only insert and remove from the top.
    - Unlike a queue where we can insert to the front and remove the end.
* Similar to a stack and queue, we can also implement using a Python list.
* See `Deque.py` and `DequeTest.py`.

```
Deque

   addRear-->               <--addFront
             [ , , , , ,   ]
              0         n-1
<--removeRear               removeFront-->

```

# Linked Lists

* Python lists are just one way to implement a list-type data structure.
* The underlying structure of a Python list stores information contiguously (in memory).
    - This is why certain operations like inserting into index 0 requires shifting elements to make room.
* There is another way to implement a list data structure that performs better in certain operations (and worse in others).
    - Linked lists do not organize data contiguously in memory, so maintaining the list structure doesn't need to shift elements around.
* __Linked Lists_ are list data structures that are not stored in contiguous memory, but still provides relative positioning of the data in the list.

## Node

* A `Node` is an item in the Linked List.
* A Node containts the data that we are storing in the list and a "reference" to the next Node in the Linked List.

## Linked List

* A `LinkedList` manages and maintains the chain of nodes as a list collection.
* It contains a _head_ reference to the first node in the linked list chain.
    - As long as we know where the first element is, we can walk down the Linked List and visit every node in the collection.
* Methods in the Linked List class should maintain the links between nodes.
    - These methods maintain the "links" between the nodes in order to keep the Linked List structure in a valid state.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next = newNext

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    # def addToFront(self, item):

    # def length(self):

    # def search(self, item):

    # def remove(self, item):
```
