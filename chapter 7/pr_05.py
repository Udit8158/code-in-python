# Date:08/08/2021
# Printing sum of natural numbers till givven number
num=int(input("Enter a number:\n"))
s=0
for i in range(1,num+1):
    s=s+i

print('sum of all natural numbers till '+str(num) +' = '+ str(s))
    