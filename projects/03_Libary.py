# Date:25/08/2021

# Make a class Libary
class Libary:
    def __init__(self,ListofBooks):     #Make a constractor to take a booklist in a Libary when it is called
        self.books=ListofBooks

    def displayAvailableBook(self):     #To display all Libary books
        print("\tAvialable books are: ")
        for book in self.books:
            print("\t    "+ book)
    
    def borrowBook(self,bookname):     #To borrow book
        if bookname in self.books:
            print(f"Thanks for borrowing the book {bookname} from our Libary")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry the given is not available right now")
            return False

    def bookReturn(self,bookname):     #To return book
        print("Thanks for returning the book in time")
        self.books.append(bookname)


    
# Making a class named student
class Student:
    def requestBook(self):
        self.book = input("Enter the name of your desire book: ")
        return self.book
    
    def returnbook(self):
        self.book = input("Enter the name of the book which you want to return: ")
        return self.book

CentralLibary = Libary(["Learn Python","Learn C++","Learn Web","Learn IOS","Learn Android","Learn Java"])
student = Student()
while (True):
    welcomeMsg = '''****WELCOME TO CENTRAL LIBARY****
          Your options are:
            Press 1 to see all available books in our Libary
            press 2 to borrow any book
            press 3 to add or return any book
            press 4 to exit from our libary
    '''
    print(welcomeMsg)
    press = int(input("Enter your choice: "))
    if press == 1:
        CentralLibary.displayAvailableBook()
    elif press == 2:
        CentralLibary.borrowBook(student.requestBook())
    elif press ==3:
        CentralLibary.bookReturn(student.returnbook())
    elif press == 4:
        break
    else:
        print("Please enter a valid option")
