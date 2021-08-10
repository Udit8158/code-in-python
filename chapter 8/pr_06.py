# Date:10/08/2021
# Conveting from inches to cms
def conv(inch):
    return (inch*2.54)
i=int(input("Enter a value in inches to convert it into cms: "))
print(i,"inches =",conv(i),"cms")