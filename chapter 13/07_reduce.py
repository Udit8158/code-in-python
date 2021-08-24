# Date:24/08/2021
from functools import reduce
mult = lambda a,b:a*b
lis = [1,2,3,4]

val = reduce(mult,lis)
print(val)      #reduce function do rolling operation

val2=reduce(mult,lis,3)
print(val2) #It prints 72

sum = lambda a,b:a+b
val3 = reduce(sum, lis,3)
print(val3)    #It adds extra 3