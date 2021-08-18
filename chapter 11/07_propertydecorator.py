# Date:18/08/2021

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

    @totalsalary.setter
    def totalsalary(self,value):
        print(self.salarybonous==self.salary-value)
Ramu= Employee()
Ramu.totalsalary
Ramu.changesalarybonous(1500)
Ramu.totalsalary       #now total salary is changed
Ramu.totalsalary=11500
totalsalary(11500)