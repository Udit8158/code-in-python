# Date:15/08/2021
# Again take the example of Employee
class Employee:
    company="Google"
    def getslary(self):
        print(f"Salary of the employee working in {self.company}  is {self.Salary} ")
Udit =Employee()
Udit.Salary="40LPA"
# Employee.getslary(Udit)  #This is same as below line.
Udit.getslary()

