#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 19:34:23 2022

@author: ilyasabdulrahman
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something:  ")
    # r = r.adjust_for_ambient_noise(source, duration=5)
    audio = r.listen(source, timeout=2)
    
    try:
        text = r.recognize_google(audio).lower()
        print("You said: {}".format(text))
    except:
        print("Sorry could you repeat that again?")