import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sun raha hoon bhai...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return command.lower()
    except:
        speak("Samajh nahi aaya bhai")
        return ""

def main():
    speak("Hello Harshit bhai, kaise madad karu?")
    while True:
        query = listen()
        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Bhai, time ho raha hai {time}")
        elif "youtube" in query:
            webbrowser.open("https://youtube.com")
            speak("YouTube khol diya bhai")
        elif "stop" in query:
            speak("Chal bhai, milte hai")
            break

main()
