#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 22:23:41 2022

@author: ilyasabdulrahman
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:38:56 2022

@author: ilyasabdulrahman
"""

import speech_recognition as sr
from translate import Translator

translator1= Translator(to_lang="Spanish")
translator2= Translator(from_lang="spanish",to_lang="english")

r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Person 1, please speak:  ")
        audio1 = r.listen(source)
        text1 = r.recognize_google(audio1).lower()
        if text1 == "stop":
            print("You have stopped the conversation")
        translation1 = translator1.translate(text1)
        print(translation1)
        print("Person 2, please speak: ")
        audio2 = r.listen(source)
        text2 = r.recognize_google(audio2, language="sp-SP").lower()
        translation2 = translator2.translate(text2)
        print(translation2)
except:
    print("Sorry, I could not understand what you were saying")