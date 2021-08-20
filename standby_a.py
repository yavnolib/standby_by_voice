# -*- coding: utf-8 -*-
import os
import sys
from pynput.keyboard import Key, Listener
import time
import pyttsx3
from tkinter import *
count=0

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

def quit():
    global root
    root.quit()
def speak(what):
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
def on_release(key):
    global count
    if key == Key.end:
        count+=1
    if count == 5:
        speak("Компьютер будет выключен через несколько секунд")
        os.system('shutdown -s')
        sys.exit()
def on_press( key):
    print(key)
        ## # Collect events until released


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
