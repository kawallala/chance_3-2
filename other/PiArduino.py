from serial import*
from Tkinter import*
from webbrowser import*
from time import*
import random 

ser = Serial('/dev/ttyACM1', 9600)

def fd():
     ser.write("Fd.")

def left():
     ser.write("Lf.")
     
def staph():
     ser.write("St.")

def right():
     ser.write("Rt.")

def bd():
     ser.write("Bd.")

tinicial= int(time())



vent = Tk()






marco1 = Frame(vent)
marco1.pack()

fd = Button(marco1, width=20,text="Adelante",command=fd)
fd.pack()


marco2 = Frame(vent)
marco2.pack()

left = Button(marco2, width=20,text="Izquierda",command=left)
left.pack(side=LEFT)

stop = Button(marco2, width=20,text="Detenerse",command=staph)
stop.pack(side=LEFT)

right = Button(marco2, width=20,text="Derecha",command=right)
right.pack(side=LEFT)

marco3 = Frame(vent)
marco3.pack()

Bd = Button(marco3, width=20,text="Atras",command=bd)
Bd.pack()

marco4 = Frame(vent)
marco4.pack(side=LEFT)

acelerometro = Label(marco5, text="              Acelerometro =" )
acelerometro.pack(side=LEFT)

acce = Label(marco5, text='')
acce.pack(side=LEFT)

marco5 = Frame(vent)
marco5.pack(side=LEFT)

hora = Label(marco5, text="              Tiempo =" )
hora.pack(side=LEFT)

rolex = Label(marco5, text='')
rolex.pack(side=LEFT)


 
tiles_letter = ['']

def add_letter():
    tiempo = str( int(time()) - tinicial -1)
    rand = random.choice(tiles_letter) + tiempo
    rolex.config(text=rand)  
    vent.after(500, add_letter)
    


vent.after(0, add_letter)  

vent.mainloop()



