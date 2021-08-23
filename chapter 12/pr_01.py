# Date:23/08/2021
# Creating three files
with open('1.txt','w') as f:
    f.write("This is 1 number file")
with open('2.txt','w') as f:
    f.write("This is 2 number file")
# with open('3.txt','w') as f:
#     f.write("This is 3 number file")

try:
    with open('1.txt','r') as f:
        f.read()
    with open('2.txt','r') as f:
        f.read()
    with open('3.txt','r') as f:
        f.read()
except:
    print("Any of these 3 file is not present")
