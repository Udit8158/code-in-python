# Date:22/08/2021
#Local and global variables

n=43   #global
def change():
    global n   #Using global and by writting this we change the global value so see the statement 3
    print(f"statement 1 {n}")
    n=32   #using a local variable and now the global value is equal to the local
    print(f"statement 2 {n}")


change()
print(f"statement 3 {n}")