
from pygame import mixer
from tkinter import *
import os

def Playsong():                        #functions defining features of player
    livesong = playlist.get(ACTIVE)
    print(livesong)
    mixer.music.load(livesong)
    songstatus.set('Playing')
    mixer.music.play()

def Pausesong():
    songstatus.set('Pause')
    mixer.music.pause()

def Stopsong():
    songstatus.set('Stop')
    mixer.music.stop()

def Resumesong():
    songstatus.set('Resume')
    mixer.music.unpause()

root = Tk()                    #creates windows
root.title('Erock')

mixer.init()
songstatus = StringVar()
songstatus.set('Choosing')

playlist=Listbox(root,selectmode=SINGLE,bg="#AFF5D4",fg="black",font=('Cambria',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\Krishna\Desktop\Python_classes&inheritance\Music_player\song')
songs = os.listdir()                      #os module to access song in folder
for i in songs:
    playlist.insert(END, i)

#variables for buttons in player
Playbtn = Button(root, text='Play', command=Playsong)
Playbtn.config(font=('Cambria',15),bg="#5CA684",fg="white", height=3, width=7, padx=7,pady=7)
Playbtn.grid(row=2,column=0)

Pausebtn = Button(root, text='Pause', padx=10, command=Pausesong)
Pausebtn.config(font=('Cambria',15),bg="#5CA684",fg="white", width=7,height=3,padx=7,pady=7)
Pausebtn.grid(row=2,column=1)

Stopbtn = Button(root, text='Stop', padx=10, command=Stopsong)
Stopbtn.config(font=('Cambria',15),bg="#5CA684",fg="white",height=3,width=7, padx=7,pady=7)
Stopbtn.grid(row=2,column=2)

Resumebtn = Button(root, text='Resume', padx=10, command=Resumesong)
Resumebtn.config(font=('Cambria',15),bg="#5CA684",fg="white",height=3,width=7, padx=7,pady=7)
Resumebtn.grid(row=2,column=3)

root.mainloop()


