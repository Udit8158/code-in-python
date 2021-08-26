# Date:25/08/2021

def divissible(number):
    if number%5==0:
        return True
    else:
        return False

listofnumbers=[3,5,20,25,23,234]
newlist=list(filter(divissible,listofnumbers))
print(newlist)