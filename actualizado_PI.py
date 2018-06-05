from serial import*
from Tkinter import*
from webbrowser import*
from time import*
import random 

ser = Serial('/dev/ttyACM0', 9600)    #Para cuando estas en la pi
#ser = Serial('/dev/tty.usbserial', 9600)    #Para cuando no estas en la pi
tinicial= int(time())



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

def prender1():
     global pto
     pto = 1
     
def apagar1():
     global pto
     pto = 0          

def prender2():
     global tem
     tem = 1
     
def apagar2():
     global tem
     tem = 0          


vent = Tk()

global pto 
pto = 0

global tem
tem = 0

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

si1 = Button(marco4, text="Prender",command=prender1)
si1.pack(side=LEFT)

no1 = Button(marco4, text="Apagar",command=apagar1)
no1.pack(side=LEFT)

acelerometro = Label(marco4, text="Acelerometro =" )
acelerometro.pack(side=LEFT)

acce = Label(marco4, text="")
acce.pack(side=LEFT)

marco5 = Frame(vent)
marco5.pack(side=LEFT)

hora = Label(marco5, text="Tiempo =" )
hora.pack(side=LEFT)

rolex = Label(marco5, text="")
rolex.pack(side=LEFT)

marco6 = Frame(vent)
marco6.pack()

si2 = Button(marco6, text="Prender",command=prender2)
si2.pack(side=LEFT)

no2 = Button(marco6, text="Apagar",command=apagar2)
no2.pack(side=LEFT)

temperatura = Label(marco6, text="Temperatura=" )
temperatura.pack(side=LEFT)

temper = Label(marco6,text="")
temper.pack(side=LEFT)
 
tiles_letter = ['']

def add_letter():
     
     tiempo = str( int(time()) - tinicial -1)
     rand = random.choice(tiles_letter) + tiempo
     rolex.config(text=rand)
     vent.after(500, add_letter)

def lectura():
     if pto == 1:
          ser.write("AC.")
          a = '['
          if ser.read() == '[':          
               for x in range(0,15):
                    a = a + ser.read()
               acce.config(text=a)
          vent.after(1000, lectura)
     if pto == 0:
          acce.config(text="Desactivado")
          vent.after(1000, lectura)

def temp():
     if tem == 1:
          ser.write("TP.")
          a = ""
          if ser.read() == '[':
               for x in range(0,10):
                    if ser.read() == ']':
                         break
                    a = a + ser.read()
               a = a + '°'
               temper.config(text=a)
          vent.after(1000,temp)
     if pto == 0:
          temper.config(text="Desactivado")
          vent.after(1000, temp)

     
vent.after(0, add_letter)  
vent.after(1000, lectura)  
vent.after(1000,temp)

vent.mainloop()
