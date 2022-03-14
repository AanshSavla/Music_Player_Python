# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:07:25 2020

@author: User
"""

import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("JK MUSIC PLAYER")
root.geometry("800x400+10+10")
root.config(bg="black")
#root.minsize(800,400)
#root.mainloop()

listofsongs=[]
realnames=[]
global index
index=0

def directorychooser():
    
    directory = askdirectory()
    
    os.chdir(directory)
    for file in os.listdir(directory):
       
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            audio=ID3(realdir)# for metadata
            realnames.append(audio["TIT2"].text[0])
            listofsongs.append(file)
            
    
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    
    
    
def nextsong(event):
    global index
    global v
    try:
        index+=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index=0
        pygame.mixer.music.load(listofsongs[0])
        pygame.mixer.music.play()
    
def prevsong(event):
    global index
    global v
    try:
        index-=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index=len(realnames)-1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        
def stopsong(event):
    pygame.mixer.music.stop()
    
    

label=Label(root,text="Music Player",width=20,font=("arial",28,"bold"),background="cadet blue",fg="gold")
label.place(x=10,y=10)


directorychooser()


listbox=Listbox(root,width=65,font=("arial",10,"bold"),background="black",fg="gold")
listbox.place(x=10,y=60)
realnames.reverse()
print(realnames)
for items in realnames:
    listbox.insert(0,items)
    



nextbutton = Button(root,text="Next Song",width=16,font=("Monotype Corsiva",16,"bold"),fg="blue")
nextbutton.place(x=20,y=290)

previousbutton = Button(root,text="Previous Song",width=16,font=("Monotype Corsiva",16,"bold"),fg="blue")
previousbutton.place(x=240,y=290)

stopbutton = Button(root,text="Stop Music",width=16,font=("Monotype Corsiva",16,"bold"),fg="blue")
stopbutton.place(x=80,y=350)





nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

canv=Canvas(root,width=200,height=200,bg="black",highlightthickness=0)
canv.place(x=500,y=50)
photo=ImageTk.PhotoImage(Image.open("img.jpg"))
canv.create_image(20,20,anchor=NW,image=photo)
root.mainloop()