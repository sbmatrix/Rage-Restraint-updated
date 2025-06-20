import cv2
from deepface import DeepFace
from tkinter import *
from PIL import Image, ImageTk
import tkinter, os
import time
from s import * # Tkinter code in here

angryCount = 0

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while video.isOpened():
    _, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Grayscale then use face detection
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in face:
        image = cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 1)
        try:
            analyze = DeepFace.analyze(frame, actions=['emotion']) # Call deepface library
        
            dictionary = analyze[0]

            emotion = dictionary['dominant_emotion'] # Get emotions from deepface

            print(emotion)

            if(emotion == "angry"): 
                angryCount = angryCount + 1
                print(angryCount)
                if(angryCount < 17): # Stage 1
                    if(angryCount == 8 or angryCount == 10 or angryCount == 15):
                        angryCount = 17
                        print("Running stage 1")
                        stage1()
                        print("done")
                
                elif(angryCount < 43): # Stage 2
                    
                    if(angryCount == 25 or angryCount == 25 or angryCount == 30 or angryCount == 35 or angryCount == 40):
                        angryCount = 50
                        print("Running stage 2")
                        stage2()
                
                elif(angryCount >= 58): # Stage 3
                    
                    # Dont call stage3 in s file
                    # Instead impliment it here for
                    # 0 command to get out

                    notPressed = True
                    win = Tk()
                            
                    win.attributes('-alpha', 0.0) # Set window to clear
                    win.iconify()

                    window = Toplevel(win) # Get toplevel from windows
                    
                    offsetL = (win.winfo_screenwidth() - 1700)/2
                    offsetT = (win.winfo_screenheight() - 956)/2 # Calculate offsets of image
                    window.geometry("1700x956+" + str(int(offsetL)) + "+" + str(int(offsetT)))
                    window.overrideredirect(1)

                    Time = 60 # Time to lock screen
                    win.after(Time * 1000, lambda: win.destroy())
                    
                    # Load photo 
                    photo = tkinter.PhotoImage(file="stage3.png")

                    label = Label(window, image=photo, text=str(Time), fg="Orange", compound="center", font=("Helvetica", 70))
                    label.pack()
                    window.attributes("-topmost", True)
                    keepGoing = True
                    while keepGoing: # While 0 not pressed
                        try:
                            label.config(text=secondsToText(Time))
                            win.update_idletasks()
                            win.update() # Update tkinter
                            time.sleep(1) 
                            Time -= 1
                            key = cv2.waitKey(1) # On 0 exit
                            if key == ord('0'):
                                keepGoing = False
                                angryCount = 0
                                win.destroy()
                        except:
                            keepGoing = False
                            angryCount = 0 # Set count to 0
                            win.destroy()
        
        
                    """while(notPressed):
                        key = cv2.waitKey(1)
                        if key == ord('0'):
                            notPressed = False"""
                    

            
        except:
            print('no face')


    cv2.imshow('video', frame) # Show frame as window
    key = cv2.waitKey(1)
    if key == ord('0'):
        angryCount = 0

video.release() 
cv2.destroyAllWindows() # Just in case - destory window on exit


"""

Judges, Look Angry!!!

"""