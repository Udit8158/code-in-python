# Date:18/08/2021
class Person:        #Parrent class
    age=17
    def getinfo(self):
        print("I am a boy")

class Programmer(Person):  #Child_1 class
    company="Google"
    def pgetinfo(self):
        print(f"I am a programmer of {self.company}")

class Employee(Programmer):   #Child_2 class
    age=23
    company="Microsoft"
p=Person()
# print(p.company)   #Throws an error because a prarent class cant use atributes of a child class

pr=Programmer()
print(pr.company)
print(pr.age)     #Print 17 as a child class can use a atribute of a parrent class.
e=Employee()
e.pgetinfo()
print(e.company)