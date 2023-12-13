from datetime import datetime
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from threading import Thread
import time
from joblib import load
import wikipedia
import random


class IntentHandler:
    def __init__(self, model_path='intent.joblib'):
        # Load your trained model here
        self.intent_recognition_model = load(model_path)

        self.intent_functions = {
            "greeting": self.greet,
            "search": self.search,
            "calculate": self.calculate,
            "bye": self.bye,
            "tell_joke": self.joke,
            "wikipedia": self.wiki,
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
        searchResult = wikipedia.search(query)
        print(searchResult)
        # Search Wikipedia for the query
        # page_py = wiki_wiki.page(query)

        if len(searchResult) > 0:
            try:
                # If the page exists, get the summary
                wikiPage = wikipedia.page(searchResult[0])
            except wikipedia.DisambiguationError as error:
                wikiPage = wikipedia.page(error.options[0])
            print(wikiPage.title)
            summary = str(wikiPage.summary[:300])
            # summary = page_py.summary[:300]  # Limiting the summary to the first 300 characters for brevity
            return f"Here is what I found on Wikipedia: {summary}"
        else:
            return "I couldn't find information on that topic in Wikipedia."



    def joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "How does a penguin build its house? Igloos it together!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"
        ]

        random_joke = random.choice(jokes)
        return random_joke

    def unknown(self):
        return "I'm not sure how to handle that."

    def handle_intent(self, intent, query=None):
        intent_function = self.intent_functions.get(intent, self.unknown)
        if intent == "wikipedia":
            return self.wiki(query)
        else:
            return intent_function()

    def recognize_intent(self, speech):
        # Replace this with your actual intent recognition logic using the loaded model
        # For simplicity, assume the model returns the probabilities of each class
        predicted_probs = self.intent_recognition_model.predict_proba([speech])[0]
        print("Predicted Probabilities:", predicted_probs)

        # Use argmax to get the index of the class with the highest probability
        predicted_intent_index = predicted_probs.argmax()

        # Get the classes (intents) from the model
        classes = self.intent_recognition_model.classes_

        # Get the predicted intent based on the index
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
