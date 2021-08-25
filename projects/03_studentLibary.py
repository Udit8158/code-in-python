# Date:25/08/2021

class Libary:
    def __init__(self,ListofBooks):
        self.books=ListofBooks

    def displayAvailableBook(self):
        for book in self.books:
            print(f"\tAvialable books are :{book}")
    
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"Thanks for borrowing the book {bookname} from our Libary")
            self.books.remove(bookname)
        else:
            print("Sorry the given is not available right now")

    def bookReturn(self,bookname):
        print("Thanks for returning the book in time")
        self.books.append(bookname)

       
class Student(Libary()):
    def __init__(self,name):
        self.name=name

    def requestBook(self,reqbookname):
        if reqbookname in self.books:
            print("Yes your desire book is available in our libary\nIf you wanted to purchase {reqbookname} please confirm your order")
        else:
            print("Sorry your desire book is not availble in our libary write now")



centrallibary=Libary(["Learn Python","Learn Web","Learn IOS","Learn Android"])
centrallibary.displayAvailableBook()
centrallibary.borrowBook("Learn Python")
centrallibary.displayAvailableBook()
centrallibary.bookReturn("Learn Python")
centrallibary.displayAvailableBook()

# udit=Student("Udit",["Learn Python","Learn Web","Learn IOS","Learn Android"])
# udit.requestBook("Learn Web")
