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
print(leapyearfinder(givven_year))