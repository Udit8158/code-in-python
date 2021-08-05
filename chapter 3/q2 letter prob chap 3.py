# Date:30/07/21
letter=''' Dear<[Name]>
 CONGRATULATION,
    I am happy to say that         
             You are selected
             <Date>'''

name=input("Please entr your name:\n")
date=input("Please enter date:\n")
letter=letter.replace("Name",name)  # Here we do replace
letter=letter.replace("Date",date)
print(letter)
