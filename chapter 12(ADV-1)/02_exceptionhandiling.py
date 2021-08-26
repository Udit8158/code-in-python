# Date:21/08/2021
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    print(num1/num2)
except ZeroDivisionError:
    print("You can't devide a number by zero")
except ValueError:
    print("Enter a vailtd number")    #In this way we can mention a error in except statement to print individual statement for a individual error
except:
    print("You are doing somethig wrong")  #This is for any other kind of error

#Always remember you must write a code after try or except statements.