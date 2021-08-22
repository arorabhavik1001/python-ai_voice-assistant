import datetime
from gtts import gTTS
import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randrange
import subprocess

def speak(text):
    # will speak based on whatever text is provided
    tts = gTTS(text=text, lang='en',slow=False, tld="ca")
    filename ='output.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def wishUser():
    # will wish the user and start the conversation
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<22:
        speak("Good Evening")
    speak("I am Luna, your virtual AI voice assistant made by bhavik in python. Please tell me how may i help you")

wishUser()

def takeCommand():
    # will take mic input from user and returns a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

while True:
    query = takeCommand().lower()
    
    # execute tasks based on the command
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        print(results,"\n")
        speak(f"According to wikipedia {results}\n")
    elif 'open youtube' in query:
        speak("Opening YouTube...")
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        speak("Opening Google...")
        webbrowser.open('google.com')
    elif 'open whatsapp' in query:
        speak("Opening Whatsapp...")
        webbrowser.open('web.whatsapp.com')
    elif 'open website' in query:
        qq = query.split(' ')
        speak(f"Opening {qq[2]}...")
        webbrowser.open(qq[2])
    elif 'say hare krishna' in query:
        speak(f"Hare Krishna")
    elif 'is krishna' in query:
        speak(f"Oh! Krishna is the Absolute Truth and the primeval cause of all causes. He will soon be appearing on the 31st of august.")
    elif 'open my study material' in query:
        speak("Opening Your Study Material...")
        webbrowser.open('https://nios.ac.in/online-course-material/sr-secondary-courses.aspx')
    elif 'play music' in query:
        speak("Playing Music...")
        music_dir = "/home/bhavik/Music"
        musics = os.listdir(music_dir)
        webbrowser.open(os.path.join(music_dir, musics[randrange(len(musics))]))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"The time is {strTime}")
    elif 'the date' in query:
        strdate = datetime.datetime.now().strftime("%d")
        strmonth = datetime.datetime.now().strftime("%B")
        stryear = datetime.datetime.now().strftime("%Y")
        speak(f"It is the {strdate}th of {strmonth} {stryear}")
    elif 'open code' in query:
        subprocess.run(["code"])
        speak("Opening Visual Studio Code")
    elif 'bye bye' in query:
        speak("Nice talking to you. See you soon.")
        break
    else:
        speak("Sorry, that feature is not supported yet. Please try something else. I can play music, search wikipedia, tell date and time, open websites.")
        continue
