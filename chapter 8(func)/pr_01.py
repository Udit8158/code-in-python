# Date:09/08/2021

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))


def greatest(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
      
    elif num2>num1:
        if num2>num3:
            return num2
    else:
        return num3         
print(greatest(num1,num2,num3))



