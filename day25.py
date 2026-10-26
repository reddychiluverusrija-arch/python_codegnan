import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
recogniser=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    print('Assistant:', text)
    engine.say(text)
    engine.runAndWait()
#listen function
def listen():
    with sr.Microphone() as mic:
        audio=recogniser.listen(mic)
        try:
            text=recogniser.recognize_google(audio)
            print("you:", text)
            return text.lower()
        except sr.UnknownValueError:
            speak("I am unable to understand, please speak again")
            return " "
        except sr.RequestError:
            speak("I am unable to connect to the server")
            return ''
print('hi welcome to voice assistant, how can i help you')
while True:
    command=listen()
    # saying hi
    if 'hello' in command:
        speak('Hi, how can i help you?')
    elif 'time' in command:
        curtime=datetime.now().strftime('%I:%M:%p')
        speak('current time is:'+curtime)
    elif 'open google' in command:
        speak('opening google')
        webbrowser.open('http://www.google.com')
    elif 'open youtube' in command:
        speak('opening youtube')

        webbrowser.open('http://www.youtube.com')
    elif 'search' in command:
        command =command.replace('search','',1)
        speak='searching for'+command
        # speak(url)
        webbrowser.open('http://www.google.com/search?q='+command)
    elif 'exit' in command:
        break
