import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index to select different voice
    engine.setProperty('rate', 150)  # Speed of speech
    eel.DisplayMessage(text)    
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing....')
        eel.DisplayMessage("recognizing...")   
        query = r.recognize_google(audio, language='vi-VN ')
        print(f"user said: {query}\n")
        eel.DisplayMessage(query)
        time.sleep(1)
        
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def allcommand():
    try:

        query = takecommand()
        print(query)

        if "open" in query:
            from engine.features import opencommand
            opencommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("i dont run")
    except:
        print("Error")
    eel.DisplayHood()
