# Date:19\08\2021
#Generating a lottery type system by using python
import random  #Importing Random

lowRange = 1
highRange = 40  #Defining Range to chose the user's number
randomNo= random.randint(lowRange, highRange)  #Generating a random range
turnsToFind = 10  #Defining user's turn

# print(randomNo) # It only use for emergency.
print(f"Hi,\nI am a guess game system\nPlease Enter your guess between {lowRange} to {highRange}")

userguess=None
userturn=0

while (userguess!=randomNo):       #condition for stop the loop
    try:
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
    # except:
    #      if userguess=="q":
    #         print("Thanks for using our game")
            # break
    except:
            print("Something went wrong\nPlease enter a valid number")
    
    
#Open a file to save the high score
# with open('E:\\Python\\projects','r') as f:
#     Highscore=int(f.read())
# #condition to save the high score
# if userturn<Highscore:
#     print(f"Oh!You just broke high score and your new score is {userturn} number of guesses. ")
#     with open('E:\\Python\\projects','w') as f:
#         f.write(str(userturn))

    
with open('Highscore.txt','w') as f:
    f.write('100000')
with open('Highscore.txt','r') as f:
    Highscore=int(f.read())

if Highscore>userturn:
    print("Congratulation you break the highscore")
    with open('Highscore.txt','w') as f:
        f.write(str(userturn))
