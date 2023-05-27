from datetime import datetime
from logging.config import listen
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#Speech engine initialization

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) #0 for male 1 for female
activationWord = "droid"


def speak(text, rate=120):
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
        listener = sr.Recognizer()
        print("Listening for a command")

        with sr.Microphone() as source:
            listener.pause_threshold = 2
            input_speech = listener.listen(source)

        try:
            print("Recognizing speech...")
            query = listener.recognize_google(input_speech, language='en_gb')
            print(f"The input speech was: {query}")

        except Exception as exception:
            print("I did not quite catch that")
            speak("I did not quite catch that")
            print(exception)
            return "None"

        return query

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    speak("Droid at your service now, Sir.")

    while True:

        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            if query[0] == "say":
                if "hello" in query:
                    speak("Greeting, everyone.")
                else:
                    query.pop(0) #Remove say
                    speech = " ".join(query)
                    speak(speech)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
