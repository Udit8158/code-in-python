# Date:25/08/2021

# Explore datetime module

import datetime
a=datetime.datetime.now()
print(a)    #This print currect date and time

#Others
print(a.strftime("%B"))  #This print Month in full form
print(a.strftime("%b"))  #This print Month in short form
print(a.strftime("%a"))  #This print DAY in short form
print(a.strftime("%A"))  #This print Month in full form
print(a.strftime("%m"))  #This print Month in numaric form