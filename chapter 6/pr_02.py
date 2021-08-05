# Date:05/08/2021
m1=int(input("Enter your first sub marks:\n"))
m2=int(input("Enter your second sub marks:\n"))
m3=int(input("Enter your third sub marks:\n"))
# Assuming exams are in 100 marks

if m1>=33 and m2>=33 and (m1+m2+m3/3)>=40:
    print("You are pass")
else:
    print("You are fail")

