# Date:17/08/2021

# The previous example is the example of this single inheritance
class Employe:           #It is the Parrent class or called base class
    company="Google"
    slary="30 LPA"
    def location(self):
        print("Location of Head Quator is Hydrabad")

class Programmer(Employe):     #It is called Derived class or called child class
    salary="40 LPA"
    def getinfo(self):
        print("He is so good ")

Harry=Employe()     #Here for Harry we can only use Parrent class's atributes.
Udit=Programmer()
print(Udit.salary)
print(Harry.slary)
Udit.location()
Udit.getinfo()   #Here we can use the atributes of both classes