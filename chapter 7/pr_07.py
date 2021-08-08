# Date:08/08/2021
#printing a pattern star


for i in range(3):    #means 0 to 4
    print(" "*(2-i),end="")
    print("*"*(2*i+1),end="")  #end is used to print in same line
    print(" "*(2-i))