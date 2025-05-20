from playsound import playsound   
from shlex import quote          
import eel
from engine.config import ASSISTANT_NAME
from engine.helper import extract_search_term, remove_words
from engine.command import speak
import os
import pyaudio
import struct
import pywhatkit as kit
import webbrowser
import sqlite3
import pvporcupine
import time
import subprocess
import pyautogui
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# playing assistant sound function
@eel.expose # Expose the function to JavaScript

def playAssistantSound():
    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)
def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()
    if app_name != "":
        try:
            cursor.execute('SELECT path from sys_command WHERE name IN (?)', (app_name,))
            result = cursor.fetchall()

            if len(result) != 0:
                speak("Opening " + query)
                os.startfile(result[0][0])\
                
            elif len(result) == 0:
                cursor.execute('SELECT path from sys_command WHERE name IN (?)', (app_name,))
                result = cursor.fetchall()

                if len(result) != 0:
                    speak("Opening " + query)
                    webbrowser.open(result[0][0])
                else:
                    speak("Opening " + query)
                    try:
                        os.system('start' + query)
                    except:
                        speak("Sorry, I am unable to open " + query)
        except Exception as e:
            speak('Something wnet wrong!')
def PlayYoutube(query):
    search_term = extract_search_term(query)    
    speak("Playying" + search_term + "on youtube")
    kit.playonyt(search_term)

def hotWord():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format = pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)

        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            keyword_index = porcupine.process(keyword)
            if keyword_index >= 0:
                print("Keyword Detected")

                import pyautogui as pg
                pg.keyDown("Win")
                pg.press("j")
                time.sleep(2)
                pg.keyUp("Win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


def findContact(query):
    words_to_remove = ['make', 'a', 'phone', 'call', 'to', 'send', 'message', 'whatsapp']
    query = remove_words(query, words_to_remove)
    try:
        query = query.strip().lower()
        cursor.exucute('SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?', ('%' + query + '%', '%' + query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+84'):
            mobile_number_str = '+84' + mobile_number_str
        return mobile_number_str, query
    except:
        speak('The contact is not in the list')
        return 0,0
def whatapps(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "Sending message to " + name
    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "Calling " + name
    else:
        target_tab = 6
        message = ''
        jarvis_message = 'Starting a video call with ' + name
    
    encoded_message = quote(message)

    whatapps_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start """{whatapps_url}"'
    subprocess.run(full_command, shell = True)
    time.sleep(5)
    subprocess.run(full_command, shell = True)
    pyautogui.hotkey('ctrl','f')
    for i in range(target_tab):
        pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    speak(jarvis_message)    
