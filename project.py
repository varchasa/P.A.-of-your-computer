import pyaudio,sys
import os
import pyttsx3
import webbrowser
import random
import pygame
import speech_recognition as sr
import unicodedata
import ctypes
import sys
import time
from time import ctime
import wave

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        time.sleep(5)
        print('could not understand audio')

    except sr.RequestError as e:
        time.sleep(5)
        print("Recog Error: {0}".format(e))

    return ""
def greeting():
    k=random.choice(["welcome sir"])
    speak(k)
    
def chrome():
    speak('got it sir')
    speak('searching for the required application')
    speak('configuring all dlls')
    speak('application found')
    speak('starting google chrome for u sir')
    os.system('start chrome.exe')
    
def internet():
    speak('got it sir')
    speak('searching for the required application')
    speak('configuring all dlls')
    speak('application found')
    speak('starting internet explorer for u sir')
    os.system('start iexplore.exe')
    
def firefox():
    speak('I heard you')
    speak('finding the firefox application')
    speak('application is brower')
    speak('starting mozilla firefox')
    os.system('start firefox.exe')

    
def onenote():
    speak('ok sir')
    speak('requested application is a microsoft package')
    speak('joining required files')
    speak('starting one note')
    os.system("start ONENOTE.EXE")
    


def notepad():
    speak('ok sir')
    speak('requested application is a text editor')
    speak('joining required files')
    speak('starting notepad')
    os.system('start notepad.exe')



def excel():
    speak('ok sir')
    speak('requested application is a microsoft package')
    speak('joining required files')
    speak('starting microsoft excel')
    os.system("start excel.exe")

def powerpoint():
    speak('ok sir')
    speak('requested application is a microsoft package')
    speak('joining required files')
    speak('starting microsoft powerpoint')
    os.system("start powerpnt.exe")

def folder():
    speak('ok sir')
    speak('requested application is a quick access')
    os.system("start explorer.exe")
    

def media():
    speak("good choice sir")
    speak("connecting to player")
    speak("connected to player")
    speak("start wmplayer.exe")
    speak("what do i play for u")
    #os.startfile('tera mera rishta.wav')
    w=wave.open("audio.mp3","r")
    speak('okay sir playing tera mera rishta for u')

def shutdown():
    speak('got it sir')
    speak('asking for permission from operating system')
    speak('permission granted')
    speak('connecting to command prompt')
    speak('connected to command prompt')
    speak('okk sir shutting down')
    os.system("shutdown /s /t 1")

def restart():
    speak('understoood sir')
    speak('asking for permission from operating system')
    speak('accessing files')
    speak('accessing all files')
    speak('accessed all files')
    speak('establishing connection to command prompt')
    speak('connecton established')
    speak('okk sir your computer is restarting     wait a moment')
    os.system('shutdown /r /t 1')

def logoff():
    speak('i heard u sir')
    speak('asking for permission from operaing system')
    speak('connection established')
    speak('i am logging off ur computer')
    ctypes.windll.user32.LockWorkStation()

def stop_shutdown():
    speak('okk sir connecting')
    speak('shutdown is cancelled')
    os.system('shutdown ~s')

def getonline():
    speak('okk sir')
    width=1360
    height=900
    img=pygame.image.load('jarvis.jpg')
    display=pygame.display.set_mode((width,height))
    crashed=2
    while crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed=false
                pygame.quit()
                sys.exit(0)
                quit()
        display.blit(img,(0,0))
        pygame.display.update()
        speak('connecting to remote servers')
        speak('establishing secure connections')
        speak('starting all systems')
        speak('downloding and installing required drivers')
        speak('just a second sir')
        speak('')
        speak('now i m online sir')
        break

def gooffline():
    speak('as you wish sir')
    speak('disconnecting to all servers')
    speak('goodbye')
    #quit()
    exit()



def mainfunction(source):
    r=sr.Recognizer()
    speak('say something!!')
    print("say something !! ")
    print()
    audio=r.listen(source)
    user=r.recognize_google(audio)
    print("you said : ",user)
    
    if user in ["open onenote"," open microsoft one note","one note","microsoft one note"]:
        onenote()
    elif user in ["open publisher","publisher","microsoft publisher","microsoft pulisher"]:
        publisher()
    elif user in ["open outlook","Outlook","microsoft outlook","microsoft outlook"]:
        outlook()
    elif user in ["open Internet","Internet"]:
        speak('which browser you want sir , chrome, firefox, internet explorer')
        
    elif user=="Google Chrome":
        chrome()
    elif user=="Firefox":
        firefox()
    elif user=="Internet Explorer":
        internet()
    elif user=="down":
        gooffline()
    elif user in ["folder","open folder", "open quick access","quick access"]:
        folder()
    
    elif user in ["notepad","open Notepad"]:
        notepad()
    elif user=="Excel":
        excel()
    elif user=="PowerPoint":
        powerpoint()
    
    elif user=="song":
        media()
    elif user in ["log off", "lock my PC","lock"]:
        logoff()
    elif user=="Olivia":
        getonline()
    elif user in ["thank you","thanks", "thank you Olivia","thanks Olivia"]:
        greeting()
    elif user in ["hi","hey","hello","whatsup","good morning","sup"]:
        a=random.choice(["hi","hey","hello","whatsup","good morning","sup"])
        speak(a)
    elif user in ["good morning","noon"]:
        b=random.choice(["hi", "sup", "good afternoon", "hello", "hey"])
        speak(b);
    elif user in ["good night", "night","exit","quit"]:
        c = random.choice(["bye", "good night", "yeah you should sleep"])
        speak(c)
        logoff()
    elif user in ["what is the time"]:
        speak(ctime())
        print(ctime())
    elif user=="shutdown":
        shutdown()
    
        
        
def loop():
    if __name__ == "__main__":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while 1:
                try:
                    mainfunction(source)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                    sys.exit()
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    sys.exit()
                

loop()

input()


