# Date:05/08/2021
text=input('Enter a comment: \n')

if 'make a lot of money' in text:      #in is used for see is the commint contaning the text.
    print('This is a spam')
elif 'buy now' in text:
    print('This is a spam')
elif 'sulicrite this' in text:
    print('This is a spam')
elif 'click this' in text:
    print('This is a spam')
else:
    print("This is not spam you can trust")