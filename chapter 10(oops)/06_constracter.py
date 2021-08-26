# Date:15/08/2021
class Employee():
    company="Google"
    def __init__(self,Salary,Adress,age,name):     #Init is a special type of function it automitically print this line
        print(f"New employee is created in {self.company}")
        self.Salary=Salary
        self.Adress=Adress
        self.age=age
        self.name=name    #In this way we can do this multiple things
        


    def information(self):
        print(f"salary of {self.name} is {self.Salary}")
        print(f"salary of {self.name} is {self.Adress}")
        print(f"salary of {self.name} is {self.age}")
       
Udit=Employee("50LPA","WEST BENGAL",22,"Udit")
Employee.information(Udit)  #or  Udit.information