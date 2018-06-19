import socket
from Tkinter import*
from time import*
import random 

tinicial= int(time())

host = '172.29.1.1'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


def fd():
  s.send(str.encode("Fd."))
  
def left():
  s.send(str.encode("Lf."))
  
def staph():
  s.send(str.encode("St."))
  
def right():
  s.send(str.encode("Rt."))
  
def bd():
  s.send(str.encode("Bd."))
  
def prender1():
     global pto
     pto = 1
     
def apagar1():
     global pto
     pto = 0          

vent = Tk()

global pto 
pto = 0

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

si = Button(marco4, text="Prender",command=prender1)
si.pack(side=LEFT)

no = Button(marco4, text="Apagar",command=apagar1)
no.pack(side=LEFT)

acelerometro = Label(marco4, text="Acelerometro =" )
acelerometro.pack(side=LEFT)

acce = Label(marco4, text="      ")
acce.pack(side=LEFT)

marco6 = Frame(vent)
marco6.pack()

temperatura = Label(marco6, text="Temperatura=" )
temperatura.pack(side=LEFT)

temper = Label(marco6,text="      ")
temper.pack(side=LEFT)

hora = Label(marco6, text="Tiempo =" )
hora.pack(side=LEFT)

rolex = Label(marco6, text="")
rolex.pack(side=LEFT)



def add_time():
  tiempo = str( int(time()) - tinicial -1)
  rand = tiempo
  rolex.config(text=rand)
  vent.after(500, add_time)


def sensor():
  s.send(str.encode("Se."))
  men = s.recv(1024)
  print(men.decode('utf-8'))
  
  vent.after(3000, sensor)
  
vent.after(0, add_time)  
vent.after(0, sensor)
vent.mainloop()
print("se ha cerrado la ventana")

s.close()
