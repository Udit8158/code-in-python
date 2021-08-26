# Date:20/08/2021
#coppying pr 05
class Vector:
    def __init__(self, vec):
       self.vec = vec
    
    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
        if len(v1)!=len(v2):
            return "You can't add"   
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
            return sum
        if len(v1)!=len(v2):
            return "You can't multiply"
    def __len__(self):      #For returning length
        return len(self.vec)
    

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])

if len(v1)!=len(v2):
    print()
print(v1+v2)
print(v1*v2)
print(len(v2))