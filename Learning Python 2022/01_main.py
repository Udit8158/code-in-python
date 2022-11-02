print("Hello world")

a = 4
b = 3
sum = a + b
print(type(a))  # type checking
# print("Sum is ->", a + b)
print(f"Sum is -> {sum}")  # f string

# You can change a variable
a = 3
print(a)

# Type casting
a = 2  # int
b = 3.2  # float
sum = a + b  # float  -> Implicit type casting
c = int(sum)
print(sum, type(sum))
print(c, type(c))  # int -> 5
print(type(str(c)))  # string "5"

age = 9

# IDENTATION IN PYTHON
if (age >= 18):
    print("You can drive")
else:
    print("You can't drive")

# String
name = "Udit"
print(name[0])  # Accessing string elements
print(name.__len__())  # Length of string

# string slicing
print(name[0:3])  # print 0,1,2 index
print(name[0:4:2])  # har 2 dusri ko jump karega

# negative indexing
lastIndex = name.__len__() - 1
print(lastIndex)
print(name[-1])  # 't'
print(name[lastIndex::-1])  # inverse a string

# strings are immutable -> you can't change its index
name2 = name.replace("U", "J")  # returing a new updated string
print(name, name2)

# comparision
print(3 == 5)  # false -> boolean

print("My name is " + name)  # string concadination
print(name*10)  # print 10 times name

# Cheeck in string same like in List or dict
print("U" in name)  # True
