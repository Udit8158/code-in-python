# Date:24/08/2021
name="Udit"
Class="12"
work="coding"
age="17"

# Using f string
print(f"I am {name} and I am doing {work} now and also I am student of class {Class} whose age is {age}")

# Using .format
print("I am {} and I am doing {} now and also I am student of class {} whose age is {}".format(name,work,Class,age))

# Changing order of variables   Inter change name and work by using there index
print("I am {1} and I am doing {0} now and also I am student of class {2} whose age is {3}".format(name,work,Class,age))

# Rearrange in right way
print("I am {1} and I am doing {3} now and also I am student of class {2} whose age is {0}".format(age,name,Class,work))




