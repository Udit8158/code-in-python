# Date:08/08/2021
# n!=1X2X3X...Xn



num=int(input("Enter a number:\n"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("The factorial of "+ str(num) +" is = "+str(factorial))
