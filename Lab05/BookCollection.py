from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def getNumberOfBooks(self): 
        current = self.head
        cnt = 0
        while current :
            cnt += 1
            current = current.getNext()
        return cnt

    def insertBook(self, book):
        current = self.head
        pre = None
        dn = False
        while current != None and not dn:
            if current.getData() > book:
                dn = True
            else:
                pre = current
                current = current.getNext()
        temp = BookCollectionNode(book)
        if pre == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            pre.setNext(temp)
    
    def getBooksByAuthor(self,author):
        current = self.head
        bs = ""
        while current != None:       
            if current.getData().getAuthor().lower() == author.lower():
                bs += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return bs
 
    def getAllBooksInCollection(self):
        current = self.head
        all_books = ""
        while current != None:
            all_books += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return all_books

    def removeAuthor(self, author):
        current = self.head
        prev = None
        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                if prev == None:
                    self.head = current.getNext()
                else:
                    prev.setNext(current.getNext())
                current = current.getNext()
            else:
                prev = current
                current = current.getNext()

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        if bookNode.getData().getTitle().lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.next)

