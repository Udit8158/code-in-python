#  date 28/07/21 
# There are are few operators in python
# ARITHMARIC OPERATORS
num_1=4;num_2=6
print(num_1+num_2) # to add
print(num_1-num_2) #to substract
print(num_1*num_2) #to multiply
print(num_1//num_2)  #return an integer after devide
print(num_1/num_2) #return an float after devide
print(num_1%num_2) #To get remainder two number.
# to devide we always get a float number
d=num_1/num_2
print(type(d)) #this is the prove.
# operators are always use between variables

# ASSINGMENT OPERATOR
a=4 #this is equal to operator
a+=4 #this is for adding extra number in a
a-=2 #this for extra substract
a*=10#for extra multiply
a/=5 # for extra devide afer devide we always give a float in python
print(a)

# Comparission operator
# comparision operator always reurn bolean vaue
b=(4==3)
print(b)
c=(4>=3)
print(c)
d=(4<=3)
print(d)
e=(5!=5)
print(e)
# Logical operators
# It also return bolean value
b1=True;b2=False
print("The value of b1 and b2 is:",(b1 and b2))
print("The value of b1 or b2 is:",(b1 or b2))  
print("The value of not b2 is:",(not b2))  #it return opposite value and only defined for one varible
