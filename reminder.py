import datetime
import time
import speech_recognition as sr
import pyttsx3
import schedule

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def reminder_task(message):
    speak(f"Reminder: {message}")

def set_reminder():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Speak your reminder message:")
        audio = recognizer.listen(source)

    try:
        reminder_message = recognizer.recognize_google(audio)
        speak(f"Reminder message: {reminder_message}")

        speak("Speak the reminder time (HH:MM AM/PM):")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        reminder_time_str = recognizer.recognize_google(audio)

        reminder_time = datetime.datetime.strptime(reminder_time_str, "%I:%M %p")
        current_time = datetime.datetime.now()
        time_difference = (reminder_time - current_time).total_seconds()

        if time_difference <= 0:
            speak("Invalid reminder time. Please speak a future time.")
            return

        # Schedule the reminder task
        schedule.every().day.at(reminder_time_str).do(reminder_task, reminder_message)

        speak(f"Done, reminder set for {reminder_time_str}")
        print(f"\nReminder: {reminder_message} at {reminder_time_str}")

        while True:
            schedule.run_pending()
            time.sleep(1)

    except sr.UnknownValueError:
        speak("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
    except ValueError:
        speak("Invalid time format. Please speak the time in HH:MM AM/PM format.")

# Uncomment the line below to test the set_reminder function
# set_reminder()
