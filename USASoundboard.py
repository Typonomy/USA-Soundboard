import playsound
import tkinter as tk

folderpath=".\Sounds"

boowav="\\Boos.wav"
shortcheer="\\ShortCheer.wav"
clapwhistle="\\ClapsAndWhistling.wav"
laughwav="\\laugh.wav" 
booUSA="\\BoosandShortUSA.wav"
LongCheerUSA="\\CheersandLongUSA1.wav"
shortUSA="\\ShortUSA.wav"


root=tk.Tk()
root.geometry("650x200")

def boousasound():
    sound=folderpath+booUSA
    playsound.playsound(sound)

def cheersound():
    sound=folderpath+shortcheer
    playsound.playsound(sound)

def endcheersound():
    sound=folderpath+LongCheerUSA
    playsound.playsound(sound)

def clapwhistlesound():
    sound=folderpath+clapwhistle
    playsound.playsound(sound)

def boosound():
    sound=folderpath+boowav
    playsound.playsound(sound)

def usasound():
    sound=folderpath+shortUSA
    playsound.playsound(sound)

def laughsound():
    sound=folderpath+laughwav
    playsound.playsound(sound)


BooUSA=tk.Button(root, text="Boo-USA", command=boousasound)
BooUSA.grid(column=0, row=1,padx=20, pady=10)
boobutton=tk.Button(root, text="Boo", command=boosound)
boobutton.grid(column=1, row=1,padx=10, pady=10)
cheerbutton=tk.Button(root, text="Short Cheer", command=cheersound)
cheerbutton.grid(column=2, row=1,padx=10, pady=10)
ClapWhistlebutton=tk.Button(root, text="Clap Whistle", command=clapwhistlesound)
ClapWhistlebutton.grid(column=3, row=1,padx=10, pady=10)
USAbutton=tk.Button(root, text="Short USA", command=usasound)
USAbutton.grid(column=4, row=1,padx=10, pady=10)
laughbutton=tk.Button(root, text="Laugh", command=laughsound)
laughbutton.grid(column=5, row=1,padx=10, pady=10)
EndCheerbutton=tk.Button(root, text="End Cheer", command=endcheersound)
EndCheerbutton.grid(column=6, row=1,padx=10, pady=10)

root.mainloop()



