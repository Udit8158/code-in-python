# Date:10/08/2021
import random

def gameWin(comp,you):
    if comp=="s":
        if you=="s":
            return None
        elif you=="w":
            return False
        else:
            return True
    elif comp=="w":
        if you=="s":
            return True
        elif you=="w":
            return None
        else:
            return False
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True
        else:
            return None    
    else:
        print("Entered a valid option")    
    
print("Comp: turns Sanake(s),Water(w),Gun(g)")
randomno=random.randint(1,3)
if randomno==1:
    comp="s"
elif randomno==2:
    comp="w"
elif randomno==3:
    comp="g"

you=input("Yours turn:Sanake(s),Water(w),Gun(g)?")
print("computet choose :",comp)
w=gameWin(comp, you)
if w == True:
    print("You won!")
elif w== False:
    print("You loose!")
elif w== None:
    print("The game is tie!")
else:
    print("Entered a valid option")    