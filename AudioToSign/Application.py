import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
def func():
        r = sr.Recognizer()
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1) 
                i=0
                while True:
                        print("Listening")
                        audio = r.listen(source)
                        try:
                                a=r.recognize_google(audio)
                                a = a.lower()
                                print('Audio Recognized: ' + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='close app' or a.lower()=='close application'):
                                        print("Closing Application")
                                        break
                                else:
                                    for i in range(len(a)):
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.png'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(1)
                                                    else:
                                                            continue

                        except:
                               print(" ")
                        plt.close()
                        r.adjust_for_ambient_noise(source, duration=1) 
while 1:
  msg="Voice to Sign"
  choices = ["Recognize","Close"] 
  reply   = buttonbox(msg,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
