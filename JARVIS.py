import os
import sys

import speech_recognition as sr
import webbrowser
# ------------------------------------------------------
import openai

from dotenv import load_dotenv as ld
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")

models = openai.Model.list()
# print(models)


def ai_response(my_task):
    copletion =openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"ROLE": "user", "content": my_task}]
    )
    return copletion



# -----------------------------------------------------------
import pyttsx3
engine = pyttsx3.init()


def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


talk("Hello")
r = sr.Recognizer()

def command():
    global r

    with sr.Microphone() as source:
        print("Say")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language="ru-RU").lower()  # ru-RU
        # task = r.recognize_google(audio, language="uk-UA").lower()
        print("You: " + task)

    except sr.UnknownValueError:
        talk("Don't understand")
        task = command()

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

    else:
        # print(handle_input(input("You: ")).choices[0].message.content)
        try:
            ai_res = ai_response(ar_task).choices[0].message.content
            talk(ai_res)
        except openai.error.ServiceUnavailableError:
            talk("Виникла помилка, спробую ще раз")
            try:
                ai_res = ai_response(ar_task).choices[0].message.content
                talk(ai_res)
            except openai.error.ServiceUnavailableError:
                talk("Не можу обробити відповідь, запитай ще раз")
        except openai.error.RateLimitError:
            talk("попробуте через 20 секу")
            r.pause_threshold = 20
        except:
            talk("ой что то пашло не так, попробуй еще раз")


while True:
    make_something(command())

# command()