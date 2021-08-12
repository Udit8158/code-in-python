# Date:12/08/2021
def game():
    return 3443
with open('highscore.txt','r') as f:
 highscore= f.read()

score=game()
if highscore=="":
    with open('highscore.txt','w')as f:
        f.write(str(score))
elif score>=int(highscore):
    with open('highscore.txt','w') as f:
        f.write(str(score))

#Programme is done successfully cheeck the file
