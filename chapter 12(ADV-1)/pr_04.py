# Date:23/08/2021

try:
    a =int(input("Enter a number : "))
    b =int(input("Enter a number : "))
    div = a/b
    print(div)
except ZeroDivisionError:
    print("Infinity")
except:
    print("Enter a valid number")
