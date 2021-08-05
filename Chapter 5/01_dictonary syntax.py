# Date:02/08/2021

# A dict is changble but it is unodered

mydict={
  "Udit":"coder",
  "sky":"beautiful",      #we can store any kind of values(data types) in dict and we need to give coma after every word of a dict
  "list":[3,8,4],
   3:2 ,            #means here value of key 3 is 2
   'anotherdict':{"flower":"beautiful"}
}
print(mydict)
print(mydict.keys())  #It print keys of dict
print(mydict.values())   #It print values of dict  These are actually dict meth
# print(anotherdict.keys())   this throw an error

print(type(mydict))   #type of dict
print(type(mydict.keys()))   #Its type is not a list Its a dict keys type
print(type(mydict.values())) #dict values type
l=list(mydict)
print(type(l))   #doing type casting
# Determining the value of a key of a dict
a=mydict["Udit"]
print(a)
print(mydict['list'])     