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
    if userguess==randomNo:
        userturn+=1
        print(f"You entered a right guess in {userturn} turns")
        break
    
    elif userguess<randomNo:
        userturn+=1
        print(f"Enter a big number\nIt is your {userturn} turn")
        continue
    
    elif userguess>randomNo:
        userturn+=1
        print(f"Enter a small number\nIt is your {userturn} turn")
        continue
    
    
#Open a file to save the high score
with open("Highscore.txt","r") as f:
    Highscore=int(f.read())
#condition to save the high score
if userturn<Highscore:
    print(f"Oh!You just broke high score and your new score is {userturn} number of guesses. ")
    with open("Highscore.txt","w") as f:
        f.write(str(userturn))

    