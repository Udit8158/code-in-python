# Date:11/08/2021
with open("another.txt",'w') as f:
    f.write('me')
with open("another.txt",'r') as f:
    print(f.read())   
# we not to need any close the file with the 'with statement'
    
