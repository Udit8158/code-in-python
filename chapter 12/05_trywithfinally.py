# Date:22/08/2021
# Try with finally 
try:
    num=int(input('Enter a number: '))
    div= 1/num
    print(f"The division is : {div}")     #Remember that if the code through an error the statemunt inthe try donot run
    print('Just cheecking')      
except Exception as e:
    print(f"We are not successful for this error '{e}'")
    exit()
finally:
    print("This is very important line")  #For the help of finally this line always print if although programme exit.

print('cheeck this line print or not after raising error and also if programme is exit')  #If exit this line is not print