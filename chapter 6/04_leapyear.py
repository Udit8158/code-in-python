# Date:12\08\2021
# calculating a year is leapyear or not
def leapyearfinder(year):
    if year%4==0:
        return True
    elif year%4==0:
        return True
    elif year%100==0:
        return False
    else:
        return False

givven_year=int(input("Enter a year to cheeck that is that leap year or not :\n"))

y=leapyearfinder(givven_year)
if y==True:
    print('Its a leap year')
elif y==False:
    print('Its not a leap year')
# print(leapyearfinder(givven_year))