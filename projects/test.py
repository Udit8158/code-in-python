import webbrowser
from playsound import playsound
import datetime
from playsound import playsound
import os
import random
import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

randomNo = random.randint(1,10)
 
# webbrowser.open("google.com")
    
# import os
# # import random
# # randomNo = random.randint(0, 10)

# # music_dir="D:\\Music"
# # songs= os.listdir(music_dir)
# # print(songs)
# # os.startfile(os.path.join(music_dir,songs[randomNo]))
# # playsound("/D:/Music/to/'It's realme.mp3'",True)

# def add(a,b):
#     '''This is a function to add two numbers'''
#     return a+b
# print(add(4,5))
# print(add.__doc__)

# def openbrowser(site_name):
#     # speak(f"opening {site_name}")
#     webbrowser.open(site_name)

# openbrowser("google.com")
# d = datetime.datetime.now().strftime("%d")
# m = datetime.datetime.now().strftime("%B")
# y = datetime.datetime.now().strftime("%Y")
# print(d,m,y)

# playsound(r'E:\\Python\\projects\\song.mp3')
# def playmusic():
#     '''It play just random music from my given path {music_dir} by using os module'''
#     music_dir = "D:\\music"
#     songs = os.listdir(music_dir)
#     # speak("playing a random music")
#     print(songs)
#     os.startfile(os.path.join(music_dir,songs[randomNo]))

# playmusic()

def telldate():
    '''Tell full version of date using datetime module'''
    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%B")
    year = datetime.datetime.now().strftime("%Y")
    speak(day)
    speak(month)
    speak(year)



telldate()