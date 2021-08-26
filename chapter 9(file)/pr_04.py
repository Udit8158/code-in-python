# Date:13/08/2021
with open('Donkey.txt','r') as f:
    d=f.read()

d=d.replace('Donkey', '######')
with open('Donkey.txt','w') as f:
    f.write(d)