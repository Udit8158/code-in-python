# Date:09/08/2021
# n!=1*2*3*...n
#n!=n*(n-1)!
# factorial using loop
# fac=1
# n=4                   #Number which will be factorial
# for i in range(n):
#     fac=fac*(i+1)
    
# print(fac)

# factorial using function
def factorial_iter(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)             
    return fac
print(factorial_iter(4))  #Here factorial_iter is a built in function it calculate factorial from a loop

# Factrial using recursion
def factorial_recursive(n):      #Recursive is use for putting any math formula.It is also a built in function
    if n==1 or n==0:
        return 1
    return n*factorial_recursive((n-1))

print(factorial_recursive(3))



print(factorial_recursive(6))   #This also directly print 6!
# print(factorial_iter(4))      #But this gives an error