import socket
import Tkinter as Tk
import time
from PIL import Image, ImageTk

tinicial = int(time.time())

host = '192.168.42.46'
port = 10005

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host,port))

estado = 5
cam = 0
vel = 12

nombre = raw_input("Ingrese el nombre del archivo donde guardara sus datos: ")

texto = open(nombre, 'w')

def fwd():
    global estado
    estado = 8
    ESTADO.config(text="Avanzando")
    return


def let():
    global estado
    estado = 4
    ESTADO.config(text="Izquierda")
    return


def sto():
    global estado
    estado = 5
    ESTADO.config(text="Detenido")
    return


def rit():
    global estado
    estado = 6
    ESTADO.config(text="Derecha")
    return


def bwd():
    global estado
    estado = 2
    ESTADO.config(text="Retrocediendo")
    return


def speed(event):
    global vel
    a = str(fast.get())
    vel = a
    return


def camara(event):
    global cam
    a = str(fast1.get())
    cam = a
    return

vent = Tk.Tk()

img = Image.open("Fup.png")
Fup = ImageTk.PhotoImage(img)

imge = Image.open("Fdw.png")
Fdw = ImageTk.PhotoImage(imge)

imgr = Image.open("Flf.png")
Flf = ImageTk.PhotoImage(imgr)

imgt = Image.open("Frt.png")
Frt = ImageTk.PhotoImage(imgt)

imgt = Image.open("Fst.png")
Fst = ImageTk.PhotoImage(imgt)
fast = Tk.Scale(vent, from_=24, to=12, command=speed, length=420, sliderlength=50, width=50)
fast.set(12)
fast.pack(side=Tk.RIGHT)

marco1 = Tk.Frame(vent)
marco1.pack()

fdbt = Tk.Button(marco1, width=100, image=Fup, command=fwd)
fdbt.pack(side=Tk.LEFT)

marco2 = Tk.Frame(vent)
marco2.pack()

leftbt = Tk.Button(marco2, width=100, image=Flf, command=rit)
leftbt.pack(side=Tk.LEFT)

stopbt = Tk.Button(marco2, width=100, image=Fst, command=sto)
stopbt.pack(side=Tk.LEFT)

rightbt = Tk.Button(marco2, width=100, image=Frt, command=let)
rightbt.pack(side=Tk.LEFT)

marco3 = Tk.Frame(vent)
marco3.pack()

Bd = Tk.Button(marco3, width=100, image=Fdw, command=bd)
Bd.pack()

marco4 = Tk.Frame(vent)
marco4.pack()

acelerometro = Tk.Label(marco4, text="Acelerometro =")
acelerometro.pack(side=Tk.LEFT)

accel = Tk.Label(marco4, text="      ")
accel.pack(side=Tk.LEFT)

temperatura = Tk.Label(marco4, text="Temperatura =")
temperatura.pack(side=Tk.LEFT)

temper = Tk.Label(marco4, text="      ")
temper.pack(side=Tk.LEFT)

hora = Tk.Label(marco4, text="Tiempo =")
hora.pack(side=Tk.LEFT)

rolex = Tk.Label(marco4, text="")
rolex.pack(side=Tk.LEFT)

admin = Tk.Frame(vent)
admin.pack()

close = Tk.Button(admin, width=10, text="CLOSE", command=cl)
close.pack(side=Tk.LEFT)

ESTADO = Tk.Label(admin, width=10, text="Detenido")
ESTADO.pack()

giro = Tk.Frame(vent)
giro.pack()

fast1 = Tk.Scale(giro, orient=Tk.HORIZONTAL, command=camara, resolution=10, from_=-90, to=90, length=400,
                 sliderlength=50, width=50)
fast1.set(0)
fast1.pack(side=Tk.RIGHT)