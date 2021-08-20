# Date:19\08\2021
#Generating a lottery type system by using python
import random  #Importing Random

lowRange = 1
highRange = 40  #Defining Range to chose the user's number
randomNo= random.randint(lowRange, highRange)  #Generating a random range
turnsToFind = 10  #Defining user's turn

# print(randomNo)
print(f"Hi,\nI am a guess game system\nPlease Enter your guess between {lowRange} to {highRange}\nBut be careful you have only {turnsToFind} turns to do this")
userguess=None
userturn=0
while (userguess!=randomNo):       #condition for stop the loop
    userguess=int(input("Enter your guess: "))   #Take a number from user to run the game 
    #Do some conditional statements
    if turnsToFind<=1:
        print("Your turn is over")
        break
    
    if userguess==randomNo:
        print("You entered a right guess")
        break
    elif userguess<randomNo:
        turnsToFind=turnsToFind-1
        print(f"Enter a big number\nYour left only {turnsToFind} turns")
        continue
    
    elif userguess>randomNo:
        turnsToFind=turnsToFind-1
        print(f"Enter a small number\nYour left only {turnsToFind} turns")
        continue
    
    if userguess<highRange or userguess>lowRange:
        turnsToFind=turnsToFind-1
        print(f"Entered a valid guess between the limit\nYour left only {turnsToFind} turns")
        continue
    # with open("Highscore.txt","w") as f:
    #     f.write(Highscore)