import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
hour =int(datetime.datetime.now().hour)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(name):
    if hour > 12:
        speak("Hi,I am Jarvis, ")
        speak(f"Good Afternoon sir How may I help you")
    elif hour<=12:
       speak("Hi,I am Jarvis,Sir, ")
       speak(f"Good Morning sir How may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__=="__main__":
    wishme("Udit")

    while True:
        query = takeCommand().lower()
        #some logic
        if 'wikipedia' in query:
            print("Searching from wikipedia")
            query = query.replace('wikipedea','')
            result = wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)

    
    
   
    