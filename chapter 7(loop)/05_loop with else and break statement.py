# Date:07/08/2021
for i in range(0,7):
    print(i)
else:
    print('Done')


for i in range(0,7):
    print(i)
    if i==5:
     break   #Break statement is used for any loop
else:           #If loop is break before coplittig then else statement will not print
    print('Done')




for i in range(0,7):
    print(i)
    if i==5:
     break 
    print('F')   #Here this line is inside the loop


for i in range(0,7):
    print(i)
    if i==5:
     break 

print('F')   #Here this line is not inside the loop
# see the both result carefully