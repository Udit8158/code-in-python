# Date:20/08/2021
#Representing a simple vector
class Vector:
    def __init__(self,i,j,k):
        self.icap=i
        self.jcap=j
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
    
vec=Vector(7, 8, 10)
print(vec)