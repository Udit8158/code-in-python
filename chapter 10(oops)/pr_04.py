# Date:16/08/2021

# Adding by using static method.

#creating a calculator by a class
class Calculator:
    def __init__(self,num):
        self.number=num         #describe the num
    
    def square(self):
        
        print(f"square of {self.number} is {self.number **2}")
    
    def squareroot(self):
        
        print(f"squareroot of {self.number} is {int(self.number**0.5)}") #type casting in integer
    
    def cube(self):
        
        print(f"cube of {self.number} is {self.number**3}")

    
            


    
class User():
    @staticmethod 
    def greet():
        print("Hellow ")  
         
user_name=input("Enter your name :\n")

user_name = User()
user_name.greet()


givven_num = Calculator(4)
givven_num.square()
givven_num.squareroot()
givven_num.cube()