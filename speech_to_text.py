import os
import pyttsx3
import threading
import speech_recognition as sp
from colorama import Fore, init, Style
from mtranslate import translate
import datetime
import wikipedia
import pywhatkit
import webbrowser

engine = pyttsx3.init("sapi5")
init(autoreset=True)
voices = engine.getProperty("voices")
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(Fore.MAGENTA + "Sarthi: " + audio, end="", flush=True)
    engine.runAndWait()

def print_loop():
    while True:
        print(Fore.GREEN + 'Listening.....', end="", flush=True)
        print(Style.RESET_ALL, end="", flush=True)

def translate_hin_to_eng(text):
    english_text = translate(text, "en-us")
    return english_text

def speech_recognizer():
    recognizer = sp.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 3000
    recognizer.dynamic_energy_adjustment_damping = 0.020
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 1.0
    recognizer.non_speaking_duration = 0.3

    with sp.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + 'Listening.....', end="", flush=True)
            print(Style.RESET_ALL, end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Recognising....", end="", flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = translate_hin_to_eng(recognizer_text)
                    print("\r" + Fore.BLUE + "User :" + trans_text)
                    return trans_text
                else:
                    return " "
            except sp.UnknownValueError:
                speak("Say that again please")
                recognizer_text = " "
            finally:
                print("\r", end="", flush=True)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir, Let's Start the day")
    elif hour > 12 and hour < 16:
        speak("Good afternoon Sir, let's not be lazy because of lunch today")
    elif hour >= 16 and hour <= 18:
        speak("Good evening Sir")
    else:
        speak("Good evening sir or should I say night, either way let's wrap up things for you Sir")

def searchGoogle(query):
    print(f"searchGoogle called with query: {query}")
    query = query.replace("sarthi", "").replace("google search", "").replace("google", "")
    speak("This is what I found on google")
    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    except:
        speak("No speakable output available")

def searchYoutube(query):
    print(f"searchYoutube called with query: {query}")
    query = query.replace("youtube search", "").replace("youtube", "").replace("jarvis", "")
    speak("This is what I found for your search!")
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, Sir")

if __name__ == "__main__":
    # wish()
    print("")
    while True:
        query = speech_recognizer()
        print(f"Recognized query: {query}")
        if "google" in query:
            searchGoogle(query)
        elif "youtube" in query:
            searchYoutube(query)
