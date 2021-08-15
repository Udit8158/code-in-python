
import random
choice_list=['s','p','s']
def gameWin():
    if comp =='r':
        if you =='r':
            return None
        elif you =='p':
            return True
        elif you =='s':
            return False
        
    if comp =='p':
        if you =='r':
            return False
        elif you =='p':
            return None
        elif you =='s':
            return True
        
    if comp =='s':
        if you =='r':
            return True
        elif you =='p':
            return False
        elif you =='s':
            return None
        



print("Computers turn : Rock[r],Paper[p],Siser[s]")
comp=random.randint(1,3)
if comp==1:
    comp="r"
elif comp==2:
    comp="p"
if comp==3:
    comp="s"

you=input("Yours turn : Rock[r],Paper[p],Siser[s] :\n")

print(f"Computer's choice is {comp}")

if gameWin ==True:
    print("Congratulation You Won the Game")
elif gameWin == False:
    print("You Lost the Game Better Luck Next Time")
elif gameWin == None:
    print("Oh the Game Is Draw Please Try Again")
else:
    print("Please Entered a Valid Option")