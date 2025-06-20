from tkinter import Toplevel, Tk, Label
import tkinter, os, math
import time


# Convert seconds to str time (0:00)
def secondsToText(seconds): 
    if seconds == 120:
        return "2:00"
    minutes = seconds/60
    if minutes > 1:
        secondsLeft = seconds - (math.floor(minutes) * 60)
        print(seconds)
        return str(math.floor(minutes)) + ":" + str(secondsLeft)
    else:
        return str(seconds)
    

# Stage 1
def stage1():
    
    stage1Y = 0 # Y offset
    
    win = Tk()
        
    win.attributes('-alpha', 0.0) # Transparent
    win.iconify()

    # Load top level of window and append label
    window = Toplevel(win) 
    window.geometry("400x146+"+ str(win.winfo_screenwidth() - 400) + "+" + str(stage1Y))
    window.overrideredirect(1) 

    photo = tkinter.PhotoImage(file="stage1.png")

    label = Label(window, image=photo)
    label.pack()

    # Destroy after 5 sec
    win.after(5000, lambda: win.destroy())

    window.attributes("-topmost", True) # Window stays on top
    num = 0
    while True:

        try:
            win.update_idletasks()
            win.update()
            time.sleep(.0075)
            num = num + 1 # Timer, backup
            print(num)
            if(num > 680):
                return 0
        except: # Window destoryed
            print("quitting")
            return 0
    
    
    
def stage2():
    win = Tk()
        
    win.attributes('-alpha', 0.0) # Transparency
    win.iconify()

    window = Toplevel(win)
    
    offsetL = (win.winfo_screenwidth() - 753)/2
    offsetT = (win.winfo_screenheight() - 424)/2
    window.geometry("753x424+" + str(int(offsetL)) + "+" + str(int(offsetT)))
    window.overrideredirect(1)

    # Time to lock for
    Time = 10
    win.after(Time * 1000, lambda: win.destroy())
    
    photo = tkinter.PhotoImage(file="stage2.png")


    label = Label(window, image=photo, text=str(Time), fg="Orange", compound="center", font=("Helvetica", 50))
    label.pack()
    window.attributes("-topmost", True)
    while True:
        try:
            label.config(text=(str(Time)))
            win.update_idletasks()
            win.update()
            time.sleep(1)
            Time -= 1 
        except: 
            return 0
        
# Legacy - not used at all
def stage3():
    win = Tk()
        
    win.attributes('-alpha', 0.0)
    win.iconify()

    window = Toplevel(win)
    
    offsetL = (win.winfo_screenwidth() - 1920)/2
    offsetT = (win.winfo_screenheight() - 1080)/2
    window.geometry("1920x1080+" + str(int(offsetL)) + "+" + str(int(offsetT)))
    window.overrideredirect(1)

    Time = 120
    win.after(Time * 1000, lambda: win.destroy())
    
    photo = tkinter.PhotoImage(file="stage3.png")

    label = Label(window, image=photo, text=str(Time), fg="Orange", compound="center", font=("Helvetica", 70))
    label.pack()
    window.attributes("-topmost", True)
    while True: 
        try:
            label.config(text=secondsToText(Time))
            win.update_idletasks()
            win.update()
            time.sleep(1)
            Time -= 1
        except:
            return 0
        

#stage2()
