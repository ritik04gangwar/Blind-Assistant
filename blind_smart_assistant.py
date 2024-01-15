import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import requests 
from bs4 import BeautifulSoup
import pyjokes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import numpy as np 
import cv2 
import pyautogui 
import pywhatkit as pwk


def speechtxt(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()


def sptxt():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognising audio......")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Unable to listen....")
            speechtxt("Sorry but unable to hear try again")

if __name__=='__main__':

    if " hello mr assistant" in speechtxt().lower():

        while True:
            data1=speechtxt.lower()
            if 'time now' in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                speechtxt("Time right now is ")
                speechtxt(time)
            elif 'date today' in data1:
                date=datetime.date.today()
                speechtxt("Today's date is ")
                speechtxt(date)
            elif 'open youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'play song' in data1:
                add="C:\Users\Ritik Gangwar\Music"
                listsong=os.listdir(add)
                os.startfile(os.path.join(add,listsong[0]))
            elif 'exit' in data1:
                speechtxt("thank you have a nice day")
                break
            elif 'from wikipedia' in data1:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=4)
                speechtxt("According to wikipedia")
                speechtxt(result)
            elif "where is" in data1:
                data1 = data1.split(" ")
                location_url = "https://www.google.com/maps/place/" + str(data1[2])
                speechtxt("Hold on Sir, I will show you where " + data1[2] + " is.")
                maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
                os.system(maps_arg)
            elif "news headlines" in data1:
                url = 'https://www.bbc.com/news'
                response = requests.get(url) 
                total_content = BeautifulSoup(response.text, 'html.parser') 
                headlines = total_content.find('body').find_all('h3') 
                for x in headlines: 
                    speechtxt(x.text.strip())  
            elif 'joke' in data1:
                joke1=pyjokes.get_joke(language="en",category="neutral")
                speechtxt(joke1)
            elif 'change volume' in data1:
                devices = AudioUtilities.GetSpeakers()
                data1=data1.split(" ")
                x=data1[3]
                interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                currentVolumeDb = volume.GetMasterVolumeLevel()
                volume.SetMasterVolumeLevel(currentVolumeDb - x, None)
            elif 'take screeshot' in data1:
                image = pyautogui.screenshot() 
                image = cv2.cvtColor(np.array(image), 
                cv2.COLOR_RGB2BGR) 
                cv2.imwrite("image1.png", image) 
            elif 'send' in data1:
                data1=data1.split(" ")
                num=data1[1]
                Date=data1[len(data1)-2]
                Time=data1[len(data1)-1]
                try:
                    pwk.sendwhatmsg(num, data1[2:len(data1)-2], Date, Time)
                    speechtxt("Message Sent!")
                except: 
                    speechtxt("Error in sending the message")


            time.sleep(10)

    else:
        speechtxt("try saying hello mr assistant")