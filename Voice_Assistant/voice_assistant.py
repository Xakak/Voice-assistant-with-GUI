import speech_recognition as sr
import pyttsx3
import time
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import os
import sys
import pyautogui



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
   
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            return command
            


def run_alexa():
    command = take_command()
    print(command)
    
    if 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'open camera' in command:
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('camera')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.hotkey('alt', 'f4')

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com/")
    elif 'my location' in command:
        print("You are somewhere in Cadet College HassanAbdal,Attock District,Pakistan")
        talk("You are somewhere in Cadet College HassanAbdal,Attock District,Pakistan")
    elif "sign off" in command:
        talk(' alright then, I am switching off')
        print(' alright then, I am switching off')
        sys.exit()
    elif 'close google' in command:
        os.system("taskkill /f /im chrome.exe")

    elif 'open google chrome' in command:
        webbrowser.open("google.com")
    elif "sleep" in command:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        while len(joke)>35:
            joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'google search' in command:
        query = command.replace("google search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    elif 'youtube search' in command:
        query = command.replace("youtube search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    elif 'open new window' in command:
        pyautogui.hotkey('ctrl', 'n')
    elif 'open new tab' in command:
        pyautogui.hotkey('ctrl', 't')
    elif 'open download' or 'open downloads' in command:
        pyautogui.hotkey('ctrl', 'j')
    elif 'previous tab' in command:
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    elif 'next tab' in command:
        pyautogui.hotkey('ctrl', 'tab')
    elif 'close tab' in command:
        pyautogui.hotkey('ctrl', 'w')
    elif 'close window' in command:
        pyautogui.hotkey('ctrl', 'shift', 'w')

    else:
        talk('Please say the command again.')


if __name__ == "__main__":
    run_alexa()


