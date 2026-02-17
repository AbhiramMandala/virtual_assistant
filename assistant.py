#import required modules
import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser

#create engine for text to speech
engine=pyttsx3.init()
engine.setProperty('rate',175)

#speak function
def speak(text):
    print("Assistant:",text)
    engine.say(text)
    engine.runAndWait()
    
#command taking function
def take_command():
    listener=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=listener.listen(source)
        try:
            command=listener.recognize_google(audio) #audio to text
            command=command.lower()
            print("You said:",command)
            return command
        except:
            return ""
#create  run assistant function
def run_assistant():
    command=take_command()
    #in command it have time word
    if "time" in command:
        time=datetime.datetime.now().strftime("%I : %H : %p")
        speak(f"The current time is {time}")

    #date in command ,it returns the current date
    elif "date" in command:
        date=datetime.date.today()
        speak(f"Today date is {date}")
    #open notepad
    elif "open notepad" in command:
        speak(f"opening notepad")
        os.system('notepad')
    elif "open youtube" in command:
        speak(f"Opening youtube")
        webbrowser.open("https://www.youtube.com/")
    
    #search any query
    elif "hey siri" in command:
        query=command.replace("hey siri","")
        if query:
            url=f"https://www.google.com/search?q={query}"
            speak(f"Looking for {query}")
            webbrowser.open(url)
    elif "bye" in command or "stop" in command:
        speak("Ok bye bye")
        exit()
    else:
        speak("I am here to assist you,ask like open youtube,open notepad,time or date")

if __name__=='__main__':
    speak("Hey buddy hi, today I am here to assist you in open youtube,open notepad,time or date ")
    while True:
        run_assistant()