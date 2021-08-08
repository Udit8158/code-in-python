# Date:08/08/2021
num=int(input("Enter a number:\n"))
for i in range(1,11):
    a=num*i
    if i==10:
        a=list(a)
    # print(str(num)+"X"+str(a)+"="+str(a))
    print(type(a))