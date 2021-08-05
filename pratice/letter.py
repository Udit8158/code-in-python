# Date:30/07/21
letter=''' Dear<[Name]>
 CONGRATULATION,
    I am happy to say that         
             You are selected
             <Date>'''
 
name=input("Enter your name:\n")
date=input("Enter Date:\n")
letter=letter.replace("Name",name )
letter=letter.replace("Date",date )
print(letter)
# This is a customizable letter