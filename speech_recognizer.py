#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:10:27 2022

@author: ilyasabdulrahman
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Person 1, please speak:  ")
    audio1 = r.listen(source)
    print("Person 2, please speak: ")
    audio2 = r.listen(source)
    try:
        text1 = r.recognize_google(audio1).lower()
        text2 = r.recognize_google(audio2).lower()
        if text1 == text2:
            print("You both said the same phrase!")
        else:
            print("Person 1 said {}".format(text1))
            print("Person 2 said {}".format(text2))
    except:
        print("Sorry, I could not understand what you two were saying")
        