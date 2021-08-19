# Date:19\08\2021
#Generating a lottery type system by using python
import random  #Importing Random

lowRange = 3
highRange = 7  #Defining Range to chose the user's number
n = random.randint(lowRange, highRange)  #Generating a random range
turnsToFind = 5  #Defining user's turn
e = turnsToFind-1 #Just for my comfort


print(f"The unknown number was{n}")
print(f"Try to guess a number which in hidden,but the number is in range between {lowRange} to {highRange}")
print(f"You have only {turnsToFind} turns")

#Run a infinite while loop by using boolean value True 
while True:  
    g = int(input("Enter your guess:"))  #Taking a number from user  and then use some logic by if-else statements.
    if g > highRange or g < lowRange:
        print("Your number is not in givven range")
        break
    if e < 0:
        print("Your turn is over")
        break
    if g == n:
        for i in range(0,e+1):  #Trying to show the turn number where user crackit , but i can't
            print(f"You guess sucessfully in your {i} number turn")
            break
    else:
        print(f"Try again,you entered a wrong guess\nYou left {e} turns")
        e = e-1
        continue


# print(f"The unknown number was{n}")
