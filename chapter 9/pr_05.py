# Date:13/08/2021
replaceable_word=["Donkey","bad","poor"]
with open('listofreplacebalefile.txt','r')as f:
    d=f.read()
for word in replaceable_word:
    d=d.replace(word,"######")
    with open('listofreplacebalefile.txt','w')as f:
        f.write(d)