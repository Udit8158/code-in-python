# Date:23/08/2021
# Printing only third,fifth and seventh element of a list
l=[1,2,3,4,5,6,7,8,9]
for index,item in enumerate(l):
    if index == 2 or index== 4 or index == 6:
        print(f"in index {index} the value of the item is {item}")