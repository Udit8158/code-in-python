# Date:19/08/2021

# (a+bi)(c+di)=(ac-bd)+(ad+bc)i      multiplication of two complex numbers.

class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)
    
    def __mul__(self,c):
        mulrea=(self.real*c.real)-(self.imaginary*c.imaginary)
        mulimag=(self.real*c.imaginary)+(self.imaginary*c.real)
        return Complex(mulrea,mulimag)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1=Complex(3,4)
c2=Complex(2, 5)
print(c1+c2)
print(c2)
print(c1*c2)