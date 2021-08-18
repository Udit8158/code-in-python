# Date:17/08/2021
class Employee:
    company="Google"
    def getslary(self):
        print(f"Salary of the employee working in {self.company}  is {self.Salary} ")
Udit =Employee()
Udit.Salary="40LPA"
print(Udit.company)
# del company     #This function delete company class atributes so after writting this line uper line throws an error.
# del Salary
del Udit        #Simillarly deleting a object.
print(Udit.compamy)  #This line throws an error because now udit object was deleted.