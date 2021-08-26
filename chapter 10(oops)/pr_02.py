# Date:15/08/2021
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
givven_num = Calculator(4)
givven_num.square()
givven_num.squareroot()
givven_num.cube()
