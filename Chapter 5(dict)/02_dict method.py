# Date:02/08/2021
# Dict method
mydict={
  "Udit":"coder",
  "sky":"beautiful",      #we can store any kind of values(data types) in dict and we need to give coma after every word of a dict
  "list":[3,8,4],
   3:2 ,            #means here value of key 3 is 2
   'anotherdict':{"flower":"beautiful"}
}
keysandvalues=mydict.items()   #This function tells us the items of a dict
print("The items of mydict are:\n",keysandvalues)
keys=mydict.keys()   #This tell us the keys of a dict
print(keys)
values=mydict.values()
print(values)
updateddict=mydict.update({"float":4.5})  #Use for adding items in a dict
print(mydict)
print(mydict.get('float'))  #give the value of "float"
# same as 

print(mydict["float"])
#But if thre was no float then this function [] throws an error but mydict.get returns none value
