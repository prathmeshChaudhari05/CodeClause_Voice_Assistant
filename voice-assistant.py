from pyttsx3 import *
import speech_recognition as sr
from bs4 import *
import requests
import json
import webbrowser
import wikipedia
import datetime

e1 = Engine("sapi5")
e1.setProperty("voice", e1.getProperty("voices")[0].id)

def speak(audio):
    e1.say(audio)
    e1.runAndWait()


def greet(name):
    getTime = datetime.datetime.now().hour
    if getTime >= 0 and getTime < 12:
        return f"Good Morning {name}"

    elif getTime >= 12 and getTime < 18:
        return f"Good Afternoon {name}"

    else:
        return f"Good Evening {name}"


def takeCommand():  
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # default is 0.8
        r.energy_threshold = 200  # default is 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception:   #in any case of On Internet
        # print(e)
        print("Say that again please...")
        return "Say that again please..."

    return query


def working(query):     #user input will be compare by each task

    if "time" in query:  # Test Status : Working
        strTime = datetime.datetime.now().strftime("%I hours & %M minute")
        # speak(f"Sir the time is {strTime}")
        return f"Sir the time is {strTime}"

    elif "date" in query:
        Year = datetime.datetime.now().date().year
        Month = datetime.datetime.now().date().month
        Date = datetime.datetime.now().date().day
        # speak(f"Sir Today's Date is {Date} {Month} {Year}")
        return f"Sir Today's Date is {Date} {Month} {Year}"

    elif "Wikipedia" in query:  # Test Status : Working
            try:
                # speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "", 1)
                lis = BeautifulSoup(features="html.parser").find_all("li")
                results = wikipedia.summary(query, sentences=2)
                # speak("According to Wikipedia")
                # print(results)
                # speak(results)
                return f"According to Wikipedia. {results}"

            except wikipedia.wikipedia.WikipediaException as e:
                return f'The Term "{query}" may refer to one or more similar terms. Please Describe it more specifically.'

    elif "how are you" in query:
        # speak("I am Fine, How are you Sir ")
        return "I am Fine, How are you Sir " 

    elif "youtube" in query:      
        if "open youtube"in query:
            webbrowser.open("www.youtube.in")
            return f"Opening youtube please Hold a second"
        else:
            newQuery = query.replace("youtube", "")
            youtubeLink = "https://www.youtube.com/results?search_query="
            newUrl = youtubeLink+newQuery.replace(" ", "+").rstrip("+")
            webbrowser.open(newUrl)
            return f"Opening youtube with search query as {newQuery}"
    
    elif "exit" or "quit" in query:
        speak("Exiting the Voice Assistant Thank You")
        exit()

#driver codeŚ
speak(greet("Prathmesh"))
while True:
    task = takeCommand()
    speak(working(task))

