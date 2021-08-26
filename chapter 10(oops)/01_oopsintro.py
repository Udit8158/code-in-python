# Date:14/08/2021
# Two type of case
'''
pascalcase:   RailwayStation
camelcase:    railwayStation
for naming of a class always use PascalCase
'''
# def mult(x,y):
#     return x*y
# print(mult(4, 5))  # Using function
# Using oops multiplication of two numbers
class MultiplicationOfNumbers():
    def mult(self):
        return(self.x*self.y)

num=MultiplicationOfNumbers()
num.x=4
num.y=5
m=num.mult()
print(m)


