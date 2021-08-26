# Date:23/08/2021

num=int(input("Enter a number: "))

table = [num*i for i in range(11)]
print(table)

with open("table.txt","a") as f:
    f.write(str(table))
    f.write('\n')   #Printing in new lines