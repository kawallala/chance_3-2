## Librerias utilizadas para el funcionamientoo del robot ##

import socket  ## Nos permite conectarnos por internet ##
import Tkinter as Tk  ## Nos permite crear una ventana para la GUI ##
import time  ## Nos permite saber el "tiempo" ##
from PIL import Image, ImageTk ## Nos permite ver imagenes en la GUI ##


## Constantes utilizadas ##


## Nos dice el momento en el que abrimos nuestro programa ##
tinicial = int(time.time())


## La direccion ip de la raspberry pi, y el ppuerto por el que nos conectamos ##
host = '172.30.1.1'
port = 10001


## Creamos el socket para conectarnos al servido a travez de internet ##
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))


##Estado inicial del robot (Detenido, camar mirando al frente) ##
estado = 5
cam = 90


## Abrimos un archivo txt para insertar los datos obtenidos por el robot ##
nombre = raw_input("Ingrese el nombre del archivo donde guardara sus datos: ")

texto = open(nombre, 'w')


## Funciones para manejar el robot ##

## Estas funciones cambian la variable estado antes mencionada para hacer que el robot
## avance, gire a la derecha, se detenga, gire a la izquierda o se detenga
## respectivamente


# None -> None
def fwd():
    global estado
    estado = 8
    ESTADO.config(text="Avanzando")
    return


# None -> None
def let():
    global estado
    estado = 4
    ESTADO.config(text="Izquierda")
    return


# None -> None
def sto():
    global estado
    estado = 5
    ESTADO.config(text="Detenido")
    return


# None -> None
def rit():
    global estado
    estado = 6
    ESTADO.config(text="Derecha")
    return


# None -> None
def bwd():
    global estado
    estado = 2
    ESTADO.config(text="Retrocediendo")
    return


# Esta funcion cierra la ventana
# None -> None
def cl():
    s.send(str.encode("CLOSE"))
    vent.destroy()
    return


# Esta funcion lee el slider que hay en la ventana y cambia la variable cam 
# antes mencionada
# None -> None
def camara(event):
    global cam
    a = fast1.get()
    cam = str(90 + a)
    return


# Todas estaas funciones son las que crean objetos dentro de nuestra ventada
# (Botones, Labels y un Slider) uzando la libreria Tkinter

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

marco1 = Tk.Frame(vent)
marco1.pack()

fdbt = Tk.Button(marco1, width=100, image=Fup, command=fwd)
fdbt.pack(side=Tk.LEFT)

marco2 = Tk.Frame(vent)
marco2.pack()

leftbt = Tk.Button(marco2, width=100, image=Flf, command=let)
leftbt.pack(side=Tk.LEFT)

stopbt = Tk.Button(marco2, width=100, image=Fst, command=sto)
stopbt.pack(side=Tk.LEFT)

rightbt = Tk.Button(marco2, width=100, image=Frt, command=rit)
rightbt.pack(side=Tk.LEFT)

marco3 = Tk.Frame(vent)
marco3.pack()

Bd = Tk.Button(marco3, width=100, image=Fdw, command=bwd)
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

def add_time():
    tiempo = str(int(time.time()) - tinicial - 1)
    rolex.config(text=tiempo)
    vent.after(500, add_time)

def sensor():
    global estado,cam
    message = str(estado) + '/' + str(cam) + '/' + str(vel) 
    s.send(message)
    men = s.recv(1024)

    texto.write(men[0:len(men)-1] + '/' + str(vel) + '/' + str(time.time()-tinicial) + ']' + '\n')

    data = men[1:len(men)-1]
    data = data.split('/')

    acceleration = data[0].split(';')
    print acceleration
    acceleration[0] = str(-0.15*int(acceleration[0])+52)
    acceleration[1] = str(-0.15*int(acceleration[1])+50.01)
    acceleration[2] = str(-0.14*int(acceleration[2])+47.7)
    acceleration = acceleration[0] + " X - " + acceleration[1] + " Y - " + acceleration[2] + " Z"
    accel.config(text=str(acceleration))

    estado = data[1]

    temp = data[2]
    temp = int(temp) * 0.48828125 * 10 // 10
    temper.config(text=str(temp) + 'C')

    if estado == '8':
        print "Avanzando"
    if estado == '5':
        print "Detenido"
    if estado == '4':
        print "Izquierda"
    if estado == '6':
        print "Derecha"
    if estado == '2':
        print "Retrocediendo"

    vent.after(100, sensor)

vent.after(0, add_time)
vent.after(100, sensor())
vent.mainloop()
print("se ha cerrado la ventana")

s.close()

texto.close()
