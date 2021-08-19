# Date:19/08/2021
class Employee:
    
    salary=40000
    increment=2
    #using a property method
    @property
    def SalaryAfterIncrement(self):
        return (self.salary*self.increment)
    
    #setting a setter method to know about the increment of the slary 
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,val):
        self.increment=val/self.salary

Udit=Employee()

print(Udit.SalaryAfterIncrement)  #If you do print(Udit.SalaryAfterIncrement())  then its throw an error
Udit.SalaryAfterIncrement=75000
print(Udit.increment)