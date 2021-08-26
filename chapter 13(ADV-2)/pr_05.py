# Date:25/08/2021
from functools import reduce

# def findmax(a,b):    #we can also use this made by me function instead of max
#     return max(a,b)

lis=[1,2,3,4,6,4,7,3,8,9,6,5]
print(reduce(max,lis))
