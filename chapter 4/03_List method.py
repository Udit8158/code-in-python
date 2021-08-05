# Date:31/07/2021
# LIST METHOD
L1=[100,23,45,85,94,21]
# print(L1.sort()) #It gives a error none
L1.sort()
print(L1) # Update list to assending order This the right way
L1.reverse()
print(L1) #Reverse the new L1
L1.append(1)
print(L1)  #It add 1 in last index
L1.insert(5,2) 
print(L1) #Add 2 on 5th index

print(L1.pop(4)) #Tell the value in 4th index
L1.remove(100)
print(L1)
