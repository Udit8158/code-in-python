# Date:03/08/2021
# If-elif-else ladder
num=8
a=8

if(num>a):                         #Here bracket is also an optional thing.
    print(num,"is greater than",a)
# if(num==a):
#     print(num,"is equal to ",a)    #we can also use if elif in multimes
elif(num>a):
    print(num,"is greater than",a)
elif(num==a):                           #for givving equal to use == symbol
    print(num,"is equal to",a)
else:                  #Actually else is optional
    print(num,"is equal to",a)

if(num<a):
    print('This is not in ladder')  #In this way we also write a statement out of the if elif else ladder.