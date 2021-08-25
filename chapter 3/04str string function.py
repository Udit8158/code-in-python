# DATE:30/07/21
# String function
story="i am Udit Kundu.And I am a student of Class 12.I am also a JEE Aspirant."
print(len(story)) #to define the length
print(story.endswith("t")) #only return true or false and know the last word
print(story.count("I")) #to count any thing
print(story.capitalize()) #It capitalize first letter but do small other same letter.
print(story.find("i")) #it tell us the position of any letter but only tell us the first occurance of that letter. 
print(story.replace("u","p")) #this replace word everywhere unlike find function.

a="spd"
print(a.isalpha())    #Returns true if characters of a str is letter
print(a.isnumeric())  #Returns true if characters of a str is num
print(a.isalnum())    #Returns true if characters of a str is letter or num both