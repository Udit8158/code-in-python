# Date:10/08/2021
# SNAKE Water Gun GAME (same as rock paper siser)

import random   #Importing random module to get random no. from comp
optionlist=['s','w','g']    #option for user
# Creating a function and using some conditional statement
def gameWin(comp,you):
    if comp=="s":            #we can introduced a variable in a if statement like this(comp)
        if you=="s":
            return None
        elif you=="w":
            return False
        elif you=="g":
            return True
        else:
            return "cancelled"
    elif comp=="w":
        if you=="s":
            return True
        elif you=="w":
            return None
        elif you=="g":
            return None
        else:
            return "cancelled"
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True
        elif you=="g":
            return None
        else:
            return "cancelled"    
     
    
print("Comp turns:Sanake(s),Water(w),Gun(g)")
randomno=random.randint(1,3)
if randomno==1:
    comp="s"
elif randomno==2:
    comp="w"
elif randomno==3:
    comp="g"

you=input("Yours turn:Sanake(s),Water(w),Gun(g)?")

print("computet choose :",comp,"***")
w=gameWin(comp, you)
if w == True:
    print("******\nHurray\nYou won!\n******")
elif w== False:
    print("!!!!!!\nUnfortunately you loose!\nBetter luck next time\n!!!!!!")
elif w== None:
    print("Oh!no\nThe game is tie!\nPlease play again~~~")
else:
    print("Your choice is not acceptable\n please chose a valid option")

# cancelled is used in my own upgradation in version 2