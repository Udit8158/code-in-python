# and , or , not -> Logical operator

marks = int(input("Enter your marks [0 - 100]"))

if (marks >= 0 and marks < 30):
    print("FAIL")
elif (marks >= 30 and marks < 70):
    print("PASS WITH GRADE B")
else:
    print("PASS WITH GRADE A")


name = "Udit"
age = 18

# F string in python
print(f"My name is {name} and I am {age} years old")
