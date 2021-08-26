# Date:21/08/2021
def incriment(num):
    try:
        return 1+num
    except:
        raise ValueError("This is not a number!")
print(incriment('f')) #By this way we can create our custom error.Actually this for verry addvance programmer