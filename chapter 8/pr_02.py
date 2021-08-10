# Date:09/08/2021
def tempconvertor(t):
    return (((t*9)/5)+32)   # write the rule
    
t1=int(input("Enter a degree c temp: "))

print(t1, "degree c  = ",tempconvertor(t1),"degree f")