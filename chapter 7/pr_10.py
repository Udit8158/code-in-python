# Date:08/08/2021
num=int(input("Enter a number:\n"))
for i in range(1,11):
    a=num*i
    m=str(num)+"X"+str(a)+"="+str(a)
    m=list(m)
    m.reverse()
    print(m)
