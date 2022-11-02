from re import A


list = ["Apple", "Google", 3, 3.4]  # You can store heterogenous items
print(list)
print(list[1])  # accessing list item
print(list[0::2])  # slicing and skipping like string

list[2] = "Microsoft"  # list is mutable
print(list)
list.pop()  # remove the last element
print(list)

list2 = list  # here list2 point list in memory
# here all element of list copied in list3 in present condition
list3 = list[0:4]

print(list, list2, list3)

list[1] = "Tesla"

print(list, list2, list3)  # now list and list1 is changed but list3 is same

# itreate list using for-in

for i in list:
    print(i)


# list concadination
list4 = list + [12, 3, 33]
print(list4)

print(list*3)  # repeating all elements of list by 3 times

print("Apple" in list)  # True

# List comparision
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # true
print(a is b)  # true
print(a == c)  # true
print(a is c)  # false
