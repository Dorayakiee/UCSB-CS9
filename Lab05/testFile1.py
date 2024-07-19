from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode

# Testing Book.py
def test_getTitle():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getTitle() == "Ready Player One"

def test_getAuthor():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getAuthor() == "Cline, Ernest"

def test_getYear():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getYear() == 2011

def test_getBookDetails():
    b = Book("Ready Player One", "Cline, Ernest", 2011) 
    assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"

    b4 = Book("Divergent", "Roth, Veronica", 2011)
    assert b4.getBookDetails() == "Title: Divergent, Author: Roth, Veronica, Year: 2011"

    b5 = Book("Insurgent", "Roth, Veronica", 2012)
    assert b5.getBookDetails() == "Title: Insurgent, Author: Roth, Veronica, Year: 2012"

def test___gt__():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    b4 = Book("Divergent", "Roth, Veronica", 2011) 
    assert (b < b4) == True

    b5 = Book("Insurgent", "Roth, Veronica", 2012)
    assert (b5 > b4) == True
    
# Testing BookCollection.py
def test_isEmpty_empty():
    bc = BookCollection()
    assert bc.isEmpty() == True

    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.isEmpty() == False

def test_getNumberOfBooks():
    bc = BookCollection()
    assert bc.getNumberOfBooks() == 0

    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberOfBooks() == 4

    b4 = Book("Divergent", "Roth, Veronica", 2011)
    b5 = Book("Insurgent", "Roth, Veronica", 2012)
    bc.insertBook(b4)
    bc.insertBook(b5)
    assert bc.getNumberOfBooks() == 6

def test_getBooksByAuthor():
    bc = BookCollection()
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getBooksByAuthor("KING, Stephen") == """Title: Rage, Author: King, Stephen, Year: 1977
Title: The Shining, Author: King, Stephen, Year: 1977
Title: Cujo, Author: King, Stephen, Year: 1981
"""
    b4 = Book("Divergent", "Roth, Veronica", 2011)
    b5 = Book("Insurgent", "Roth, Veronica", 2012)
    bc.insertBook(b4)
    bc.insertBook(b5)
    assert bc.getBooksByAuthor("roth, veronica") == """Title: Divergent, Author: Roth, Veronica, Year: 2011
Title: Insurgent, Author: Roth, Veronica, Year: 2012
"""
def test_getAllBooksInCollection():
    bc = BookCollection()
    assert bc.getAllBooksInCollection() == ""

    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getAllBooksInCollection() == """Title: Ready Player One, Author: Cline, Ernest, Year: 2011
Title: Rage, Author: King, Stephen, Year: 1977
Title: The Shining, Author: King, Stephen, Year: 1977
Title: Cujo, Author: King, Stephen, Year: 1981
"""
    b4 = Book("Divergent", "Roth, Veronica", 2011)
    b5 = Book("Insurgent", "Roth, Veronica", 2012)
    bc.insertBook(b4)
    bc.insertBook(b5)
    assert bc.getAllBooksInCollection() == """Title: Ready Player One, Author: Cline, Ernest, Year: 2011
Title: Rage, Author: King, Stephen, Year: 1977
Title: The Shining, Author: King, Stephen, Year: 1977
Title: Cujo, Author: King, Stephen, Year: 1981
Title: Divergent, Author: Roth, Veronica, Year: 2011
Title: Insurgent, Author: Roth, Veronica, Year: 2012
"""
def test_removeAuthor():
    bc = BookCollection()
    assert bc.removeAuthor("king, stephen") == None
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.removeAuthor("KING, STEPHEN")
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n"
    b4 = Book("Divergent", "Roth, Veronica", 2011)
    b5 = Book("Insurgent", "Roth, Veronica", 2012)
    bc.insertBook(b4)
    bc.insertBook(b5)
    bc.removeAuthor("cline, ernest")
    assert bc.getAllBooksInCollection() == """Title: Divergent, Author: Roth, Veronica, Year: 2011
Title: Insurgent, Author: Roth, Veronica, Year: 2012
"""

def recursiveSearchTitle():
    bc = BookCollection()
    assert recursiveSearchTitle() == None

    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False

    b4 = Book("Divergent", "Roth, Veronica", 2011)
    b5 = Book("Insurgent", "Roth, Veronica", 2012)
    bc.insertBook(b4)
    bc.insertBook(b5)

    bc.removeAuthor("KING, STEPHEN")
    assert bc.recursiveSearchTitle("CUJO", bc.head) == False
    assert bc.recursiveSearchTitle("ready player one", bc.head) == True
    assert bc.recursiveSearchTitle("divergent", bc.head) == True
    assert bc.recursiveSearchTitle("INSURGENT", bc.head) == True

    bc.removeAuthor("roth, veronica")
    assert bc.recursiveSearchTitle("divergent", bc.head) == False
    assert bc.recursiveSearchTitle("INSURGENT", bc.head) == False

# Testing BookCollectionNode.py
def test_BookCollectionNodeCreation():
    n = BookCollectionNode(20)
    assert n.getData() == 20
    assert n.getNext() == None

def test_BookCollectionNodeSetData():
    n = BookCollectionNode(20)
    n.setData(200)
    assert n.getData() == 200

def test_BookCollectionNodeSetNext():
    n = BookCollectionNode(20)
    n2 = BookCollectionNode(10)
    n.setNext(n2)
    assert n.getNext() == n2