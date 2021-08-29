         ###  **** JARVIS  DESKTOP  VOICE  ASSISTENT ****  ###    Date :27/08/2021  starts....on that day.

# Impoting some required modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

# Writting some functions

def speak(audio):
    ''' 
    used for play the audio using pyttsx3 module
    '''
    engine.say(audio)
    engine.runAndWait()


def wishme(user):
    '''this used to wish and introduce itself'''
    if hour > 12 and hour<18:
        speak("Hi,I am Jarvis, ")
        speak(f"Good Afternoon {user} How may I help you")

    elif hour>=18 and hour<23:
        speak("Hi, I am Jarvis ")
        speak(f"Good evening {user} How may I help you")
    
    elif hour>=23 and hour<=6:
        speak("Hi, I am Jarvis ")
        speak(f"Good night {user} How may I help you")

    elif hour<=12 and hour>6:
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

def playmusic():
    '''It play just random music from my given path {music_dir} by using os module'''
    music_dir = "D:\\music"
    songs = os.listdir(music_dir)
    speak("playing a random music")
    print(songs)
    os.startfile(os.path.join(music_dir,songs[randomNo]))

def openbrowser(site_name):
    '''By the help of webbrowser module it search the site in browser'''
    speak(f"opening {site_name}")
    webbrowser.open(site_name)

def introduce():
    '''Jarvis introduce himself'''
    speak("Hi,I am Jarvis,a desktop voice assistent,  made by Udit on 27th July,2021 , I can do some limited number of work for you, So how can I help you sir.")

def telltime():
    '''Jarvis just speak time with the help of datetime module'''
    time_hour = datetime.datetime.now().strftime("%H")
    time_minute = datetime.datetime.now().strftime("%M")
    speak(f"The time is {time_hour}:{time_minute}")

def telldate():
    '''Tell full version of date using datetime module'''
    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%B")
    year = datetime.datetime.now().strftime("%Y")
    speak(day)
    speak(month)
    speak(year)


if __name__=="__main__":
    
    # writting some variable which are used in code 

    engine = pyttsx3.init()   #To use
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
            openbrowser("google.com")

        elif "open youtube" in query:
            openbrowser("youtube.com")
        
        elif "open github" in query:
            openbrowser("github.com")

        elif "introduce"  in query:
            introduce()

        elif "who are you" in query:
            introduce()

        elif "time"  in query:
            telltime()  

        elif "date" in query:
            telldate()
        
        elif "nothing" in query:
            speak("ok then,no problem,I always here to help you")

        elif "who made you" in query:
            speak("My master is udit,He made me")
        
        elif "play music"  in query:    #Playing music with the help of os module 
            playmusic()
        
        elif "close"  in query:            #for close
            speak(f"I am closing,Bye")
            exit()


       
    
    
   
