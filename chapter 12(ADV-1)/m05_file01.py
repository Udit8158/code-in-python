# Date:22/08/2021
#This file is made for import so name start with m .Without m you can't import from a file in python

# if __name__=="__main__":
def greet(name):
    print(f"Good morning ,{name}")

#By writting this this content will not print after importing.
if __name__=="__main__":
    greet("Udit")
    print("This is file 01")