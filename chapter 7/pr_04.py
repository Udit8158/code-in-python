# Date:08/08/2021

# Cheecking a givven number is prime or not
num=int(input("Enter a number :\n"))
prime=None  #Just declare a varible prime  
for i in range(2,num):      #Means here i is 2 to num-1
    if num%i ==0:
        num = prime
        break



if num == prime:       
    print("Yes your number is prime")
else:
     print("your number is not prime")    