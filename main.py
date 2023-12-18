from datetime import datetime
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from threading import Thread
import time
from joblib import load
import wikipedia
import random
from geopy.geocoders import Nominatim
import folium
from jokes import joke
from task_management import TaskManager
from quotes import advice
from reminder import set_reminder

class IntentHandler:
    def __init__(self, model_path='intent.joblib'):
        self.intent_recognition_model = load(model_path)

        self.intent_functions = {
            "greeting": self.greet,
            "search": self.search,
            "calculate": self.calculate,
            "bye": self.bye,
            "reminder": set_reminder,
            "tell_joke": joke,
            "quotes": advice,
            "wikipedia": self.wiki,
            "task_manager": self.task_manager,
            "unknown": self.unknown
        }

    def greet(self):
        return "Hello! I am Jasper, How can I be of help to you today?"

    def search(self):
        return "Sure, let me look that up for you."

    def calculate(self):
        return "Let me do the math for you."

    def bye(self):
        return "Goodbye!"

    def wiki(self, query):
        search_result = wikipedia.search(query)

        if len(search_result) > 0:
            try:
                wiki_page = wikipedia.page(search_result[0])
                summary = str(wiki_page.summary[:300])
                return summary
            except wikipedia.DisambiguationError as error:
                wiki_page = wikipedia.page(error.options[0])
                summary = str(wiki_page.summary[:300])
                return summary
            except wikipedia.PageError:
                return "I couldn't find information on that topic in Wikipedia."
        else:
            return "I couldn't find information on that topic in Wikipedia."
    def unknown(self):
        return "I'm not sure how to handle that."

    def task_manager(self):
        task_manager = TaskManager()
        task_manager.task_manager_menu()

    def handle_intent(self, intent, query=None):
        intent_function = self.intent_functions.get(intent, self.unknown)
        if intent == "wikipedia":
            placeholder_phrases = [
                "On it",
                "Rallying round",
                "Investigating now...",
                "Exploring the data...",
                "Searching for you...",
                "Fetching the details...",
                "In the information gathering phase...",
                "Delving into the archives...",
                "Working on that request...",
                "Scouring the resources...",
                "Compiling the data...",
                "Digging into the databases..."
            ]
            random_placeholder = random.choice(placeholder_phrases)
            assistant.speak(f"{random_placeholder}. Give me a few seconds")
            return self.wiki(query)
        else:
            return intent_function()

    def recognize_intent(self, speech):
        predicted_probs = self.intent_recognition_model.predict_proba([speech])[0]
        print("Predicted Probabilities:", predicted_probs)

        predicted_intent_index = predicted_probs.argmax()
        classes = self.intent_recognition_model.classes_
        predicted_intent = classes[predicted_intent_index]

        print(f"Predicted intent: {predicted_intent}")
        return predicted_intent


class PersonalAssistant:
    def __init__(self, activation_word="jasper"):
        self.activation_word = activation_word
        self.root = tk.Tk()
        self.root.title("Personal Assistant")
        self.label = tk.Label(self.root, text="🤖", font=("Arial", 250), fg="black")
        self.label.pack()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[0].id)  # 0 for male, 1 for female
        self.listening = False
        self.intent_handler = IntentHandler()

    def speak(self, text, rate=130):
        self.engine.setProperty("rate", rate)
        self.engine.say(text)
        self.engine.runAndWait()

    def get_response(self, speech):
        if "bye" in speech.lower():
            return self.intent_handler.handle_intent("bye")
        elif self.listening:
            recognized_intent = self.intent_handler.recognize_intent(speech)
            return self.intent_handler.handle_intent(recognized_intent, speech)
        else:
            return "Sorry, I'm not listening. Say the activation word to start."

    def parse_command(self):
        listener = sr.Recognizer()
        print("Listening for a command")

        with sr.Microphone() as source:
            listener.pause_threshold = 1
            try:
                input_speech = listener.listen(source, timeout=5)
                print("Recognizing speech...")
                query = listener.recognize_google(input_speech, language='en_gb')
                print(f"The input speech was: {query}")
                return query.lower()

            except sr.UnknownValueError:
                print("I did not quite catch that")
                self.speak("I did not quite catch that")
                return ""

    def change_color(self, color):
        self.label.config(fg=color)

    def listen_for_activation_word(self):
        while True:
            query = self.parse_command()
            if self.activation_word in query:
                self.change_color("green")
                self.speak(f"{self.activation_word} at your service now, How may I help you today.")
                self.listening = True
            elif "bye" in query:
                self.change_color("red")
                self.speak("Goodbye!")
                time.sleep(3)
                self.root.destroy()
            elif self.listening:
                response = self.get_response(query)
                self.speak(response)

    def run(self):
        activation_thread = Thread(target=self.listen_for_activation_word)
        activation_thread.start()
        self.root.mainloop()

if __name__ == '__main__':
    assistant = PersonalAssistant()
    assistant.run()
