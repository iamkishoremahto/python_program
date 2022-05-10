class Book:
    def userInput():
        bookName=input("Enter the book name : ")
        return bookName

    def addBook(b=userInput()):

        book=[]
        
        book.append(b)
    
    def showBook(book):
        for item in enumerate(book):
            print(book[item])
        


b=Book()
# b.addBook()
# b.showBook()
print(book)