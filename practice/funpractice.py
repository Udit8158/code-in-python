# def starpinting(n):
#     for i in range(0,(n)):
#         print("* "*(n-i))
#         print(" "*(2-i))
        
        
# starpinting(3)
# n=int(input("Enter a number\n"))
# def multtable(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}\n")
# multtable(n)

n1=int(input("Enter first number in our calculator:\n"))
n2=int(input("Enter second number in our calculator:\n"))

options=["+","-","*","/"]

userschoice=input("Enter your operator choice from givven choicelist:")

if userschoice=='+':
    print(f"Sum of two number givven by you is:{n1+n2}")
elif userschoice=='-':
    print(f"Difference of two number givven by you is:{n1-n2}")
elif userschoice=='*':
    print(f"Multiplication of two number givven by you is:{n1*n2}")
elif userschoice=='/':
    print(f"Division of two number givven by you is:{n1/n2}")
else:
    print("Please enter a valid option")
