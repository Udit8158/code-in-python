# Date:24/08/2021

def even(num):
    if num%2==0:
        return True
    else:
        return False

lis=[1,2,3,4,5,6,7,8,9]
# filter is used for the true statement
print(list(filter(even,lis)))