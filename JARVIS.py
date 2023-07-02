import os
import sys

import speech_recognition as sr
import webbrowser
import pyttsx3
engine = pyttsx3.init()


def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


talk("Hello")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language="en-US").lower()  # ru-RU
        # task = r.recognize_google(audio, language="uk-UA").lower()
        print("You: " + task)

    except sr.UnknownValueError:
        talk("Don't understand")
        talk = command()

        return task

def make_something(ar_task):
    if ("open" and "site") in ar_task:
        talk("ok")
        url = "https//ituniver.com"
        webbrowser.open(url)


    elif "stop" in ar_task:
        talk("Good bye")
        sys.exit()

    elif "name" in ar_task:
        talk("My name is JARVIS")

while True:
    make_something(command())

# command()