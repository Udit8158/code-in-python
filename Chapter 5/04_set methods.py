# Date:03/08/2021
##Sets Method
s=set() #This is an empty set
s.add(4) #Adding a element and we can add only a single element in a set at a time
s.add(5)
s.add(3)
s.add(4)   #A set not allowed repeation so there print
s.add(6.4)
s.add((4,5,2))   #We can add a tuple in a set as it is a unchable
# s.add({4:3})  #Throws an error
# s.add([4,3,8]) #Throws an error a set cant add list,dict because they are changeble
print(s)

print(len(s))   #Calcute number of element of a set
# print(s.remove(4))  #It gives an error None  
s.remove(4)   #Right way to remove an element 
print(s)
s.pop()   #It removes an arbitiry element
print(s)
# t={4,3,2}
# print(t)       #In max case it remove small element
# t.pop()
# print(t)
s_={4,6}
print(s.union(s_))
print(s.intersection(s_))  #For intersection and union
s.clear()
print(s)  #This clear the s set  