# Date:05/08/2021
age=int(input("Enter your age:\n"))

if age>23 and age<40:         #Print if both concditions are fullfiled.
    print("You can work with us")
elif age>23 or age<40:                     #Print if one of these conditions are fullflied.
    print("Your chance to work with us is verry lesser")
else:
    print("Sorry you cant work with us")

a=None
if a is None:        #'is' is a substied of == (while this is use for only words not for number.)
    print("yes")
else:
    print("no")