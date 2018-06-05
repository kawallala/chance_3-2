import random
import time
from Tkinter import *

tinicial = int(time.time())

root = Tk()

w = Label(root, text="GAME")
w.pack()

frame = Frame(root, width=300, height=300)
frame.pack()

L1 = Label(root, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(root, bd =5)
E1.pack(side=LEFT)

tile_frame = Label(frame, text= "")
tile_frame.pack()

tiles_letter = ['']


def add_letter():
    tiempo = str( int(time.time()) - tinicial -1)
    rand = random.choice(tiles_letter) + tiempo
    tile_frame.config(text=rand)
    root.after(500, add_letter)
 


root.after(0, add_letter)  
root.mainloop()
