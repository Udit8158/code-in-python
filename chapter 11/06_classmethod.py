# Date:18/08/2021
class Employee:
    company="Amazon"
    slary="30LPA"
    location="Hydrabad"
    # def changesalary(self,sal):        #We can change a class atribute like this 
    #     self.__class__.slary=sal
    @classmethod               #Using class method
    def changesalary(cls,sal):       #Its also do same thing
        cls.slary=sal    

Udit=Employee()
Harry=Employee()
print(Udit.slary)

# Employee.slary="40LPA"      #Also chage like this
Udit.changesalary("42 lpa")   #Changing salary in class.
print(Udit.slary)
print(Employee().slary)
print(Harry.slary)