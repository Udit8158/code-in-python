# Date:22/08/2021
# Try with else 
try:
    num=int(input('Enter a number: '))
    div= 1/num
    print(f"The division is : {div}")     #Remember that if the code through an error the statemunt inthe try donot run
    print('Just cheecking')      
except Exception as e:
    print(f"We are not successful for this error '{e}'")
else:
    print("We are successful without raising any kind of error")
# So we can see here else statement will run only when the code will not through any kind of error