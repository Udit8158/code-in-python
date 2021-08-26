# Date:18/08/2021
class Person:        #Parrent class
    age=17
    def __init__(self):
        print("Initializing Person class")
    def getinfo(self):
        print("I am a boy")

class Programmer(Person):  #Child_1 class
    def __init__(self):
        super().__init__()        #It is used to print init wala function or you can say Constructive function.
        print("Initializing Programmer class")
    company="Google"
    age=20
    def getinfo(self):
        super().getinfo()       # Actuall by doing this we add the getinfo of Person class also.
        print(f"I am a programmer of {self.company}")

class Employee(Programmer):   #Child_2 class
    def getinfo(self):
        super().getinfo()     #It helps to print all of above 3 statements from getinfo function.
        print(f"I am a employee of {self.company}")
    age=23
    company="Microsoft"
p=Person()
# print(p.company)   #Throws an error because a prarent class cant use atributes of a child class

pr=Programmer()
# print(pr.company)
# print(pr.age)     #Print 17 as a child class can use a atribute of a parrent class.
e=Employee()            #It automitically print the constructive statements.
e.getinfo()       #Printting by using super method.
# print(e.company)
