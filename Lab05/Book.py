class Book:
    def __init__(self, title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getYear(self):
        return self.year
    
    def getBookDetails(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
    
    def __gt__(self, other):
        if self.author.lower() != other.getAuthor().lower():
            return self.author.lower() > other.getAuthor().lower()
        elif self.year != other.getYear():
            return self.year > other.getYear()
        else:
            return self.title.lower() > other.getTitle().lower()