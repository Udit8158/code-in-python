# Date:05/08/2021
# a=0
# # a=a+1          #we cant do this here
# while a<=10:     #while loop is running untill the condition is going to true.
#     print(a)     #Give the space to include the print statement in the while loop
#     a=a+1          #we can do it here in the while loop
# n=int(input("Enter a number to cheeck if that is greater than 100 or not!"))
while True:   #By saying True it makes it an infinite loop
    n=int(input("Enter a number to cheeck if that is greater than 100 or not!\n"))
    if n>100:
        print("Congratulation you have entered a number which is greater than 100")

        break
    else:
        print("Try again")
        continue
