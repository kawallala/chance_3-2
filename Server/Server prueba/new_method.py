import socket
import Tkinter as Tk
from time import *
from PIL import Image, ImageTk

# Declaracion de todas las variables usadas mas adelante en el programa


# Momento en que empieza a correr el programa para saber cuanto tiempo lleva corriendo
tinicial = int(time())

# Network de ZeroTier
ZeroTier = '88503383909a8fc4'

# direccion IP del host del server y el numero de puerto usado
host = '192.168.43.46'
port = 10005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


# ###-------------------------------------------------------------------------------------------------------------- ## #
# Seteo de las globales para enviar el mensaje importante

# el string que se enviara constantemente se divide en 3 cosas, divididas por "/"
# estado -> 8 = Avanzando, 5 = Detenido, 2 = Retroceder, 4 = Izquierda, 6 = Derecha
# Cam -> Un numero entre -90 y +90 , solo se envian multiplos de 10
# Vel -> Un numero entre 12 y 24, que representa que tan rapido va el robot

estado = str(5) + str(time())
estado = estado[0]
cam = str(0) + str(time())
cam = cam[0]
vel = str(12) + str(time())
vel = vel[0:1]

# ###--------------------------------------------------------------------------------------------------------------### #
# Funciones de procesamiento de datos

def agregar(x):
    m = x[0:len(x) - 1] + '/' + str(time()) + "]"
    return m


def divide(x):
    r = x.split('/')
    return r


# Devuelve el arreglo sacandole el primer elemento

def element1(x):
    r = x[1:len(x)]
    return r


# Entrega el elemento c, en este caso lo utilizamos para sacar el primer elemento

def element2(x, c):
    r = x[c]
    return r


# Devuelve el arregl, pero sin el primer elemento

def element3(x):
    r = x[0:len(x) - 1]
    return r


# Agrega los ejes X Y y Z al string que contiene las aceleraciones

def xyz(sting):
    r = sting.split(';')
    r1 = r[0] + 'X'
    r2 = r[1] + 'Y'
    r3 = r[2] + 'Z'
    r = r1 + '-' + r2 + '-' + r3
    return r


# ###--------------------------------------------------------------------------------------------------------------### #
# Esta funcion lo que hace es cerrar completamente el servidor para que no se puedan reconectar los clientes


def cl():
    s.send(str.encode("CLOSE"))
    vent.destroy()
    return


# Abrimos este archivo de texto para guardar todos los

nombre = raw_input("Ingrese el nombre del archivo donde guardara sus datos")

texto = open(nombre, 'w')

# ###--------------------------------------------------------------------------------------------------------------### #


# Esta seccion es toda la programacion referente a la ventana de python


vent = Tk.Tk()

# ###-------------------------------------------------------------------------------------------------------### #


# Funciones para avanzar, doblar a la izquierda, detenerse, doblar a la derecha e ir en reversa.

def fd():
      estado = "8"
      state.config(text="Avanzando")
      return 


def leftt():
      estado = "4"
      state.config(text="Izquierda")
      return


def staph():
      estado = "5"
      state.config(text="Detenido")
      return
    

def right():
      estado = "6"
      state.config(text="Derecha")
      return 


def bd():
      estado = "2"
      state.config(text="Retrocediendo")
      return 


def speed(event):
      a = str(fast.get())
      vel = a
      return 


def camara(event):
      a = str(fast1.get())
      cam = a
      return 


# ###--------------------------------------------------------------------------------------------------------------### #


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


# ###--------------------------------------------------------------------------------------------------------------### #

fast = Tk.Scale(vent, from_=24, to=12, command=speed, length=420, sliderlength=50, width=50)
fast.set(12)
fast.pack(side=Tk.RIGHT)

marco1 = Tk.Frame(vent)
marco1.pack()

fdbt = Tk.Button(marco1, width=100, image=Fup, command=fd)
fdbt.pack(side=Tk.LEFT)

marco2 = Tk.Frame(vent)
marco2.pack()

leftbt = Tk.Button(marco2, width=100, image=Flf, command=right)
leftbt.pack(side=Tk.LEFT)

stopbt = Tk.Button(marco2, width=100, image=Fst, command=staph)
stopbt.pack(side=Tk.LEFT)

rightbt = Tk.Button(marco2, width=100, image=Frt, command=leftt)
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

state = Tk.Label(admin, width=10, text="Detenido")
state.pack()

giro = Tk.Frame(vent)
giro.pack()

fast1 = Tk.Scale(giro, orient=Tk.HORIZONTAL, command=camara, resolution=10, from_=-90, to=90, length=400, sliderlength=50, width=50)
fast1.set(0)
fast1.pack(side=Tk.RIGHT)


def add_time():
    tiempo = str(int(time()) - tinicial - 1)
    rand = tiempo
    rolex.config(text=rand)
    vent.after(500, add_time)


def sensor():
    #print "{}/{}/{}".format(estado,cam,vel)
    #print estado + '/' + cam + '/' + vel
    mesage = estado + '/' + cam + '/' + vel
    s.send(str.encode(mesage))
    men = s.recv(1024)

    texto.write(agregar(men) + '\n')

    data = divide(men)

    acce = element2(data, 0)
    acce = element1(acce)
    acce = xyz(acce)

    accel.config(text=str(acce))

    estado = element2(data, 1)

    temp = element2(data, 2)
    temp = element3(temp)
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
vent.after(1000, sensor)
vent.mainloop()
print("se ha cerrado la ventana")

s.close()

texto.close()
