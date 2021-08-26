# Date:22/08/2021
list1=[54,"udit",6.4]

#In this way we can print all item and their index of a list
# index=0
# for item in list1:
#     print(item,f",\tthe index of the {item} is",index)
#     index+=1

#this is called enumerate method
for index,item in enumerate(list1):
    print(item,f",\tthe index of the {item} is",index)
