from BookCollectionNode import BookCollectionNode
from Book import Book

class BookCollection:
    def __init__(self):
        self.head =None

    def isEmpty(self):
        return self.head == None
    
    def getNumberOfBooks(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.getNext()

        return count
    
    def insertBook(self, book):
        new_node = BookCollectionNode(book)
        
        if self.head is None or book > self.head.getData():
            new_node.setNext(self.head)
            self.head = new_node
        else:
            current = self.head
            previous = None
            while current is not None and not (book > current.getData()):
                previous = current
                current = current.getNext()
            
            new_node.setNext(current)
            previous.setNext(new_node)


    # def getBooksByAuthor(self, author):
    #     result = ""
    #     current = self.head
    #     while current is not None:
    #         if current.getData().getAuthor().upper() == author.upper():
    #             result += current.getData().getBookDetails() + "\n"
    #         current = current.getNext()
    #     return result

    def getBooksByAuthor(self, author):
        author_lower = author.lower()
        result = []

        current = self.head
        while current:
            book = current.getData()
            current = current.getNext()

            if book.getAuthor().lower() == author_lower:
                result.append(book)

        result.sort(key=lambda x: (x.getYear(), x.getTitle().lower()))
        output = ""
        for book in result:
            output += f"Title: {book.getTitle()}, Author: {book.getAuthor()}, Year: {book.getYear()}\n"

        return output

    def getAllBooksInCollection(self):
        result = []

        current = self.head
        while current:
            book = current.getData()
            result.append(book)
            current = current.getNext()
        result.sort(key=lambda x: (x.getAuthor().lower(), x.getYear(), x.getTitle().lower()))


        output = ""
        for book in result:
            output += f"Title: {book.getTitle()}, Author: {book.getAuthor()}, Year: {book.getYear()}\n"

        return output

    
    def removeAuthor(self, author):
        author_lower = author.lower()

        
        while self.head is not None and self.head.getData().getAuthor().lower() == author_lower:
            self.head = self.head.getNext()

        
        current = self.head
        previous = None
        while current is not None:
            if current.getData().getAuthor().lower() == author_lower:
                
                if previous is not None:
                    previous.setNext(current.getNext())
                current = current.getNext()  
            else:
                
                previous = current
                current = current.getNext()
    # def removeAuthor(self, author):
    #     current = self.head
    #     previous = None
    #     while current is not None:
    #         if current.getData().getAuthor().upper() == author.upper():
    #             if previous is None:
    #                 self.head = current.getNext()
    #             else:
    #                 previous.setNext(current.getNext())
    #             current = current.getNext()
    #         else:
    #             previous = current
    #             current = current.getNext()

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode is None:
            return False
        if bookNode.getData().getTitle().upper() == title.upper():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.next)

