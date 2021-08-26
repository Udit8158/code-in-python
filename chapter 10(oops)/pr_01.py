# Date:15/08/2021
# Creating a class to store some information of few programmers

# class Programmers:
#     company="Micsoft"
#     purpose="Programming"
#     Adress="West Bengal"
#     Language="Python"
#     Laptop="Macbook PRO M1"
#     OperatingSystem="MAC"

# John=Programmers()
# print(John.Language)

# also we can do it by:  This is a better way to store any kind of information.
class programmers:
    company="Microsoft"
    def __init__(self,salary,product):
        self.salary=salary
        self.product=product

    def details(self):
        print(f"programmers of {self.company} has a salary of {self.salary} and product is {self.product}")
udit=programmers("39LPA","Edge")
harry=programmers("45LPA","SkyType")
udit.details()
harry.details()