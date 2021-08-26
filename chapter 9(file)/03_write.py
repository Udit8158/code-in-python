# Date:11/08/2021
f=open('another.txt','w') #when we open file in write mode it open a new file and when writting it clear all and a which are written
f.write("I am modifying this")
f.close()
f_=open('another.txt','a')
f_.write("I am appending it") #when we open file in append mode and write something it dont clear existing thing but add new thig on last
f_.close()