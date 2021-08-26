# Date:09/08/2021
# Average finding function
# def avg():
#     return((num_1+num_2)/2)
# num_1=int(input("Enter a number: "))
# num_2=int(input("Enter a number: "))
# print(avg())

# marks1=[45,56,57,34]
# percentage1=sum(marks1)/len(marks1)    #This is a long way
# print(percentage1,"%")


#This is the actual use of function
# printing percent of marks by using function

def percentage(marks):
    '''The percentage function gives us percentage of marks'''  #givving a document in a function
    return(sum(marks)/len(marks))

marks1=[45,56,57,34]
marks2=[43,56,27,74,5]
percentage1=percentage(marks1)
percentage2=percentage(marks2)
print(percentage1,percentage2)

print(percentage.__doc__)  #Using doc we can esily access the document givven in the function it is very helpful when we work with lots of function in a same code. 