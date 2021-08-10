# Date:10/08/2021
# s="f df   "
# print(s.strip())  #strip function actually remove extra spaces
story="I am Udit and I am a good coder and a singer.     "
def remove_strip(str):
    return str.replace("and a singer","")   #Actually we replace here by a blank
    return str.strip
print(remove_strip(story))