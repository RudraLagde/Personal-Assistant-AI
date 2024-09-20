import speech_recognition as sp
import os
import pyttsx3
import threading
import speech_recognition as sp
from colorama import Fore, init, Style
from mtranslate import translate


engine = pyttsx3.init()
init(autoreset=True)


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
    recognizer.energy_threshold = 2500
    #speech power to be tested yet
    recognizer.dynamic_energy_adjustment_damping = 0.016
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.5
    #pause which would help machine to learn that sentence is over
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 1.0
    recognizer.non_speaking_duration = 0.4

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
                recognizer_text = " "
            finally:
                print("\r", end="", flush=True)

            os.system("cls" if os.name == "nt" else "clear")
        sp_thread = threading.Thread(target=speech_recognizer)
        print_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()

speech_recognizer()