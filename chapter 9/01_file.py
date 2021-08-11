# Date:11/08/2021
# Opening a file and see the data in Python
f=open('E:\Python\chapter 9\sample.txt','r')  #open a file by givving full path location.Here r is for read a file r=rt by default
text=f.read()  #reading a file    f.read(3) means 3 character print
print(text)    #print
f.close()      #close the file

