import os


import pyttsx3
engine = pyttsx3.init()


def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


talk("Hello")