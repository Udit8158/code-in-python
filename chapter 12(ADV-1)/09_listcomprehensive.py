# Date:22/08/2021

#make a list from a existing list with the even element
l1=[3,4,6,5,78,56,1,53,68]
# l2=[]
# for item in l1:
#     if item%2==0:
#         l2.append(item)
# print(l2)

#comprehensive way  (This is shortcut)
l2=[item for item in l1 if item%2==0]   #do in a fun way
print(l2)

#make another list with the element greater than 6 from l1

l3=[item for item in l1 if item>6]
l3.sort()  #sorting the list l3
print(l3)

l4=[1,4,3,4,2,1,6,5,5,6]
s={item for item in l4}    #Actually it remove all repeated value
print(s)  #This is call set comprehension we can also do dict comprehension
