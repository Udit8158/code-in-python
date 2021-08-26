# Date:19/08/2021
class C_2dVector:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class C_3dVector(C_2dVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap =k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
vec2d=C_2dVector(3, 5)
vec3d=C_3dVector(2, 5, 9)

print(vec2d)
print(vec3d)
    
