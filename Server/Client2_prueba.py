
import socket 
import sys

##---------------------------------------------------------------------##

from Tkinter import*
from webbrowser import*
from time import*
import random

##---------------------------------------------------------------------##

HOST='192.168.43.46'
PORT=5000
SERVER_IP = '192.168.43.46'
PORT_NUMBER = 5000
SIZE = 1024


s= socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
s.connect(( HOST, PORT ))

mySocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

tinicial = int(time())


def fd():
     mySocket.sendto("Fd.",(SERVER_IP,PORT_NUMBER))

def left():
     mySocket.sendto("Lf.",(SERVER_IP,PORT_NUMBER))
     
def staph():
     mySocket.sendto("St.",(SERVER_IP,PORT_NUMBER))

def right():
     mySocket.sendto("Rt.",(SERVER_IP,PORT_NUMBER))

def bd():
     mySocket.sendto("Bd.",(SERVER_IP,PORT_NUMBER))

def prender():
     global pto
     pto = 1
     
def apagar():
     global pto
     pto = 0          

vent = Tk()

global pto 
pto = 1

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

si = Button(marco4, text="Prender",command=prender)
si.pack(side=LEFT)

no = Button(marco4, text="Apagar",command=apagar)
no.pack(side=LEFT)

acelerometro = Label(marco4, text="              Acelerometro =" )
acelerometro.pack(side=LEFT)

acce = Label(marco4, text='')
acce.pack(side=LEFT)

marco5 = Frame(vent)
marco5.pack(side=LEFT)

hora = Label(marco5, text="              Tiempo =" )
hora.pack(side=LEFT)

rolex = Label(marco5, text='')
rolex.pack(side=LEFT)

marco6 = Frame(vent)
marco6.pack()

 
tiles_letter = ['']

def add_letter():
     
     tiempo = str( int(time()) - tinicial -1)
     rand = random.choice(tiles_letter) + tiempo
     rolex.config(text=rand)
     vent.after(500, add_letter)

#def lectura():
#    if pto == 1:
#         ser.write("AC.")
#         a = '['
#        if ser.read() == '[':          
#             for x in range(0,15):
#                  a = a + ser.read()
#            acce.config(text=a)
#       vent.after(1000, lectura)
#  if pto == 0:
#       acce.config(text="Desactivado")
#       vent.after(1000, lectura)
     
vent.after(0, add_letter)  
#vent.after(1000, lectura)  

vent.mainloop()


            
s.close()
