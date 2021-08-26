# Date:19/08/2021
class Number:
    def __init__(self,num):     #these all are dunder method
        self.num=num
                                         
    def __add__(self,num1):   #This is for adding
        return f"sum is {self.num+num1.num}"

    def __mul__(self,num1):
        return f"multiplication is {self.num*num1.num}"
    
    def __str__(self):        #It is use for  printing any thig
        return f"integer {self.num}"
    
    def __len__(self):
        return 1

n1=Number(4)
n2=Number(5)
print(n1+n2)
print(n1*n2)
print(n1)    #This line prints integer 4
print(len(n1))
