# Date:19/08/2021
class Animal:
    def __init__(self):
        pass
class Pets(Animal):
    pass
class Dog(Pets):
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"The dog {self.name} is barking")

D=Dog("Tonny")  
D.bark()    
