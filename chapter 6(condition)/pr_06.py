# Date:05/08/2021
sub=input("Enter your subject name :\n")
marks=int(input("Enter your marks in above subject :\n"))

if marks>=90 and marks<=100:
    print("Your grade is 'Ex'")
elif marks>=80 and marks<90:
    print("Your grade is 'A'")
elif marks>=70 and marks<80:
    print("Your grade is 'B'")
elif marks>=60 and marks<70:
    print("Your grade is 'C'")
elif marks>=50 and marks<60:
    print("Your grade is 'D'")
elif marks<50:
    print("Your grade is 'F'")
else:
    print("Yours marks is envalid\n please enter a valid marks to know your proper grade'")
