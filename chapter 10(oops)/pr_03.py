# Date:16/08/2021
class sample():
    a = "Google"
comp = sample()
print(comp.a)

#This is actually adding a new instance atribute.This do not change class atribute directly.
comp.a = "Microsoft"
print(comp.a)

#Changing the class atribute like this way.
sample.a= "Adobe"
comp = sample()
print(comp.a)


#so the answer of the question is no we cant do like that way.