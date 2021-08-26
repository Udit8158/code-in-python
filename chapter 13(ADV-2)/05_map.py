# Date:24/08/2021

def root(num):
    return int(num**0.5)

lis=[1,4,9,16]
l_2=[]
# Find the root of all elements in the givven list and make a list
# Method 1 without using map
for item in lis:
    l_2.append(root(item))

print(l_2)

# Method 2 with using map

print(list(map(root,lis)))  #Storing in a list


#Practice
add = lambda x:x+1
print(list(map(add,lis)))    #Actually we use map in the list
