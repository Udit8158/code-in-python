# Date:19/08/2021

class Employee:
    company="Sony"
    salary=10000
    salarybonous=2000
    # totalsalary=10000+2000   #Instead of doing this we use property decorator to access eassily
    @property
    def totalsalary(self):      #With the help of property decorator we use this totalslary function as a class atributes(property)
        print(self.salary+self.salarybonous)         #Actually this whole method is known as getter
    @classmethod      #changing salarybonous by class method
    def changesalarybonous(cls,salb):
        cls.salarybonous=salb

    @totalsalary.setter          #setter method
    def totalsalary(self,value):
        print(self.salarybonous==value-self.totalsalary)
Ramu= Employee()
print(Ramu.salarybonous)
print(Ramu.salary)
print(Ramu.totalsalary)
Ramu.changesalarybonous(3000)
print(Ramu.totalsalary)
Ramu.totalsalary=14000
print(Ramu.salarybonous)
