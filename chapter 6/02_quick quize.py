# Date:03/08/2021
# Vote determining system
print("Can I eligible for vote?")
age=input('Please enter your age:\n')
age=int(age)   #Converting into int nehito cant compare with a int 18
if(age==18):
    print("yes")
elif(age<18):
    print("no")
else:
    print("yes")