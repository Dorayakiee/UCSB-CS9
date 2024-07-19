from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection1 import BookCollection

# Test cases for Book class

def test_book_init():
    book = Book("Title1", "Author1", 2000)
    assert book.getTitle() == "Title1"
    assert book.getAuthor() == "Author1"
    assert book.getYear() == 2000

def test_book_getBookDetails():
    book1 = Book("Title1", "Author1", 2000)
    book2 = Book("Ready Player One", "Cline, Ernest", 2011)
    book3 = Book("ThisisaBook", "OOOMG", 2011)
    assert book1.getBookDetails() == "Title: Title1, Author: Author1, Year: 2000"
    assert book2.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"
    assert book3.getBookDetails() == "Title: ThisisaBook, Author: OOOMG, Year: 2011" 


def test_book_gt_operator():
    book1 = Book("Title1", "Author1", 2000)
    book2 = Book("Title2", "Author2", 2010)
    assert book2 > book1
    book3 = Book("Ready Player One", "Cline, Ernest", 2011)
    book4 = Book("ThisisaBook", "OOOMG", 2011) 
    assert (book3 < book4) == True

# Test cases for BookCollectionNode class

def test_node_init():
    book = Book("Title1", "Author1", 2000)
    node = BookCollectionNode(book)
    assert node.getData() == book
    assert node.getNext() == None

def test_node_setNext():
    book1 = Book("Title1", "Author1", 2000)
    book2 = Book("Title2", "Author2", 2010)
    node1 = BookCollectionNode(book1)
    node2 = BookCollectionNode(book2)
    node1.setNext(node2)
    assert node1.getNext() == node2

def test_node_setData():
    book1 = Book("Title1", "Author1", 2000)
    book2 = Book("Title2", "Author2", 2010)
    node1 = BookCollectionNode(book1)
    node2 = BookCollectionNode(book2)
    node1.setData(node2)
    assert node1.getData() == node2

# Test cases for BookCollection class

def test_bookcollection_init():
    bc = BookCollection()
    assert bc.isEmpty() == True

def test_bookcollection_isEmpty():
    bc = BookCollection()
    assert bc.isEmpty() == True

    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.isEmpty() == False

def test_bookcollection_insertBook_and_getNumber():
    bc = BookCollection()
    b1 = Book("Cujo", "King, Stephen", 1981)
    b2 = Book("The Shining", "King, Stephen", 1977)
    b3 = Book("Ready Player One", "Cline, Ernest", 2011)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 3

def test_bookcollection_getBooksByAuthor():
    bc = BookCollection()
    b1 = Book("Cujo", "King, Stephen", 1981)
    b2 = Book("The Shining", "King, Stephen", 1977)
    b3 = Book("Ready Player One", "Cline, Ernest", 2011)
    b4 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.insertBook(b4)
    assert bc.getBooksByAuthor("KING, Stephen") == """Title: Rage, Author: King, Stephen, Year: 1977
Title: The Shining, Author: King, Stephen, Year: 1977
Title: Cujo, Author: King, Stephen, Year: 1981
"""
    b5 = Book("ThisisaBook", "OOOMG", 2011)
    b6 = Book("NotaBook", "OOOMG", 2012)
    bc.insertBook(b5)
    bc.insertBook(b6)
    assert bc.getBooksByAuthor("OOOMG") == """Title: ThisisaBook, Author: OOOMG, Year: 2011
Title: NotaBook, Author: OOOMG, Year: 2012
"""

def test_bookcollection_getAllBooksInCollection():
    bc = BookCollection()
    assert bc.getAllBooksInCollection() == ""

    b1 = Book("Cujo", "King, Stephen", 1981)
    b2 = Book("The Shining", "King, Stephen", 1977)
    b3 = Book("Ready Player One", "Cline, Ernest", 2011)
    b4 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.insertBook(b4)
    assert bc.getAllBooksInCollection() == """Title: Ready Player One, Author: Cline, Ernest, Year: 2011
Title: Rage, Author: King, Stephen, Year: 1977
Title: The Shining, Author: King, Stephen, Year: 1977
Title: Cujo, Author: King, Stephen, Year: 1981
"""

def test_bookcollection_removeAuthor():
    bc = BookCollection()
    b1 = Book("Cujo", "King, Stephen", 1981)
    b2 = Book("The Shining", "King, Stephen", 1977)
    b3 = Book("Ready Player One", "Cline, Ernest", 2011)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.removeAuthor("KING, Stephen")
    assert bc.getNumberOfBooks() == 1
    assert bc.isEmpty() == False
    assert bc.getBooksByAuthor("KING, Stephen") == ""

def test_bookcollection_recursiveSearchTitle():
    bc = BookCollection()
    b1 = Book("Cujo", "King, Stephen", 1981)
    b2 = Book("The Shining", "King, Stephen", 1977)
    b3 = Book("Ready Player One", "Cline, Ernest", 2011)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    bc.removeAuthor("King, Stephen")
    assert bc.recursiveSearchTitle("CUJO", bc.head) == False
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False
