import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Слухаю...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="uk-UA")
            print(f"📢 Ви сказали: {text}")
            return text
        except sr.UnknownValueError:
            return "Не розпізнано"

while True:
    command = listen()
    if "стоп" in command:
        speak("Асистент завершив роботу!")
        break
    speak(f"Ви сказали: {command}")
