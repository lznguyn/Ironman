from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
from engine.command import speak
import os
import pywhatkit as kit

# playing assistant sound function
@eel.expose # Expose the function to JavaScript

def playAssistantSound():
    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)
def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query !="":
        speak("Opening" + query)
        os.system('start' + query)
    else:
        speak('not found')
def PlayYoutube(query):
    search_term = extract_search_term(query)    
    speak("Playying" + search_term + "on youtube")
    kit.playonyt(search_term)
def extract_search_term(command):

    # Extract the search term from the query
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None    