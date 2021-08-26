# Date:21/08/2021
# Using try it run the code when also the throws an error   
try:
    age=int(input("Enter your age :"))
    if age>18:
        print("You are eligible to give voot in this year")
    else:
        print("You are not eligible for voot in this year")
except Exception as e:
    print(e)      #This line print the error if happend,without breaking a efficiency of code        
        
print("Sorry you prees anythig wrong\nPlease enter a valid age")