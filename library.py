# from calendar import leapdays
# from re import U


class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.leadbook={}
    
    def DisplayBook(self):
        print(f"We have following book in our library ")
        for book in self.booklist:
            print(book)

    def LeadBook(self,user,book):
        if book not in self.leadbook.keys():
            self.leadbook.update({book:user})
            print("Lender-Book database has been updated, now you can take the book")
        else:
            print(f"Book is already being used by {self.leadbook[book]} ")


    def AddBook(self,book):
        self.booklist.append(book)

    def ReturnBook(self,book):
        self.leadbook.pop(book)
kishore=Library(['Python','C++','Java','JavaScript'],"Kishore")

if __name__ == '__main__':
    kishore=Library(['Python','C++','Java','JavaScript'],"Kishore")
    while True:
        print("welcome to the library")
        print("""
        1.Display Book List
        2.Lead Book
        3. Add Book
        4. Return Book""")
        user_input=int(input("Enter your choice : "))
        # if user_input not in [1,2,3,4]:
        #     print("Please enter a valid option")
        #     continue
        # else:
        #     user_input=int(input("Enter your choice : "))
        
        if user_input == 1:
            kishore.DisplayBook()
        elif user_input == 2:
            user=input("Enter your name : ")
            book=input("Enter book name : ")
            kishore.LeadBook(user,book)
        elif user_input == 3:
            book= input("Enter book name : ")
            kishore.AddBook(book)

        elif user_input == 4:
            book= input("Enter book name :")
            kishore.ReturnBook(book)
        else:
            print("Invailed Choice ")
        
        print(" Press q for quite and c for continue ")
        user_input2 = ""
        while(user_input2 != "q" and user_input2 != "c"):
            user_input2= input()
            if user_input2 == "q":
                exit()
            elif user_input2 == "c":
                continue
            


