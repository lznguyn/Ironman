import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index to select different voice
    engine.setProperty('rate', 150)  # Speed of speech
    print(voices)
    engine.say(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='vi-VN ')
        print(f"user said: {query}\n")
    except Exception as e:
        return ""
    return query.lower()
text = takecommand()
speak(text)