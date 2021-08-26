# Date:23/08/2021

num=int(input("Enter a number: "))
# listof10numbers = [1,2,3,4,5,6,7,8,9,10]

# mult_table = [item for item in listof10numbersitem*num]
# print(mult_table)

table = [num*i for i in range(11)]
print(table)