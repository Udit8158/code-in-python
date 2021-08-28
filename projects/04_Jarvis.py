import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


def speak(audio):
    ''' 
    used for play the audio using pyttsx3 module
    '''
    engine.say(audio)
    engine.runAndWait()


def wishme(user):
    '''this used to wish and introduce itself'''
    if hour > 12:
        speak("Hi,I am Jarvis, ")
        speak(f"Good Afternoon {user} How may I help you")
    elif hour<=12:
       speak("Hi,I am Jarvis, ")
       speak(f"Good Morning {user} How may I help you")
def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__=="__main__":
    
    engine = pyttsx3.init()
    hour =int(datetime.datetime.now().hour)
    randomNo = random.randint(0,10 )
    # user = input("Enter your name :")

    wishme("udit")
    
    while True:
        query = takeCommand().lower()
        #some logic
        # if "Ok" or "Hello" or "Hi" in query:
        #     wishme(user)
        if 'wikipedia' in query:
            print("Searching from wikipedia")
            query = query.replace('wikipedea','')
            result = wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)
        
        elif "open google" in query:   #Open any website using webbrowser module
            speak("opening google...")
            webbrowser.open("google.com")

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        
        elif "play music " or "play song" in query:    #Playing music with the help of os module 
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            speak("playing a random music")
            print(songs)
            os.startfile(os.path.join(music_dir,songs[randomNo]))
        
        elif "close" or "stop" in query:            #for close
            speak(f"I am closing")
            break

       
    
    
   
    