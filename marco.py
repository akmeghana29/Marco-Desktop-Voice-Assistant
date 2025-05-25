import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import ctypes


print('Loading your personal voice assistant - Marco')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

music_directory = "D:\Education\Projects\Virtual Assistant\Audios for Rex"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user :{statement}\n")

        except Exception as e:
            speak("Pardon, please repeat that again")
            return "None"
        return statement
    
def openFolder(folder_name):
    if folder_name == "documents":
        documents_path = os.path.expanduser("~/Documents")
        os.startfile(documents_path)
        speak("Opening Documents folder")
    elif folder_name == "downloads":
        downloads_path = os.path.expanduser("~/Downloads")
        os.startfile(downloads_path)
        speak("Opening Downloads folder")
    else:
        speak("Sorry, I can't open that folder")
        
def volumeControl(command):
    if "increase" in command:
        for _ in range(5):  # Increase volume (5 steps)
            ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)  # Volume up key code
        speak("Increasing volume")
    elif "decrease" in command:
        for _ in range(5):  # Decrease volume (5 steps)
            ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)  # Volume down key code
        speak("Decreasing volume")
    elif "mute" in command:
        # Mute system volume
        ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)  # Mute key code
        speak("System muted")
    elif "unmute" in command:
        # Unmute system volume (use the same key, since mute/unmute is a toggle)
        ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)  # Mute key code
        speak("System unmuted")
        
def takeNotes():
    notes = []
    speak("I am ready to take notes. Start dictating, and say 'save' when you're done.")
    
    while True:
        note = takeCommand().lower()
        
        if 'save' in note:
            with open("notes.txt", "a") as file:
                for line in notes:
                    file.write(line + "\n")
            speak("I've saved your notes.")
            print("Notes saved:", notes)
            break
        
        elif note == "none":
            continue  # Skip if no valid input was heard
        
        else:
            notes.append(note)  # Keep adding lines of notes
            speak("What else would you like to add?")
            print(f"Note added: {note}")
            
def readNotes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content:
                print("Your saved notes are:")
                print(content)
                speak("Here are your saved notes.")
                speak(content)
            else:
                print("No notes found.")
                speak("No notes are saved yet.")
    except FileNotFoundError:
        print("notes.txt file not found.")
        speak("There are no saved notes yet.")

    
def playMusic():
    songs = os.listdir(music_directory)  # List all songs in the music directory
    if songs:
        song = random.choice(songs)  # Randomly choose a song
        speak(f"Now playing {song}")
        os.startfile(os.path.join(music_directory, song))  # Play the song
    else:
        speak("No music files found in the directory.")

speak("Loading your personal voice assistant Marco")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you ?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "stop" in statement:
            speak('Marco is shutting down, Have a nice day')
            print('Marco is shutting down, Have a nice day')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
            
        if "open documents" in statement:
            openFolder("documents")

        elif "open downloads" in statement:
            openFolder("downloads")
            
        if "increase volume" in statement:
            volumeControl("increase")

        elif "decrease volume" in statement:
            volumeControl("decrease")

        elif "mute" in statement:
            volumeControl("mute")

        elif "unmute" in statement:
            volumeControl("unmute")
            
        elif 'take notes' in statement or 'write down' in statement:
            takeNotes()
            
        elif 'read notes' in statement or 'show notes' in statement:
            readNotes()
            
        elif 'play music' in statement:
            playMusic()

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Marco version 1 point O your persoanl assistant. I am programmed to do your tasks!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Meghana")
            print("I was built by Meghana")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions, would you like to ask something')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)