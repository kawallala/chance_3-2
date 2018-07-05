import socket
import Tkinter as tk
from time import *
from PIL import Image, ImageTk

# Declaracion de todas las variables usadas mas adelante en el programa


# Momento en que empieza a correr el programa para saber cuanto tiempo lleva corriendo
tinicial = int(time())

# Network de ZeroTier
ZeroTier = '88503383909a8fc4'

# direccion IP del host del server y el numero de puerto usado
host = '192.168.43.46'
port = 10003

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))


# ## -------------------------------------------------------------------------------------------------------------- ## #

# Funciones de procesamiento de datos

# Divide el arreglo de datos por /, para separar aceleracion estado y temperatura


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


# ###-------------------------------------------------------------------------------------------------------### #

# Funciones para avanzar, doblar a la izquierda, detenerse, doblar a la derecha e ir en reversa.

def fd():
    s.send(str.encode("Fd."))
    return sensor2()


def left():
    s.send(str.encode("Lf."))
    return sensor2()


def staph():
    s.send(str.encode("St."))
    return sensor2()


def right():
    s.send(str.encode("Rt."))
    return sensor2()


def bd():
    s.send(str.encode("Bd."))
    return sensor2()


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


vent = tk.Tk()


# ###--------------------------------------------------------------------------------------------------------------### #


img = Image.open("Fup.png")
Fup = ImageTk.PhotoImage(img)

imge = Image.open("Fdw.png")
Fdw = ImageTk.PhotoImage(imge)

imgr = Image.open("Flf.png")
Flf = ImageTk.PhotoImage(imgr)

imgt = Image.open("Frt.png")
Frt = ImageTk.PhotoImage(imgt)


# ###--------------------------------------------------------------------------------------------------------------### #


marco1 = tk.Frame(vent)
marco1.pack()

fd = tk.Button(marco1, width=100, image=Fup, command=fd)
fd.pack()

marco2 = tk.Frame(vent)
marco2.pack()

left = tk.Button(marco2, width=100, image=Flf, command=left)
left.pack(side=tk.LEFT)

stop = tk.Button(marco2, width=100, image=Frt, command=staph)
stop.pack(side=tk.LEFT)

right = tk.Button(marco2, width=100, image=Frt, command=right)
right.pack(side=tk.LEFT)

marco3 = tk.Frame(vent)
marco3.pack()

Bd = tk.Button(marco3, width=100, image=Fdw, command=bd)
Bd.pack()

marco4 = tk.Frame(vent)
marco4.pack()

acelerometro = tk.Label(marco4, text="Acelerometro =")
acelerometro.pack(side=tk.LEFT)

accel = tk.Label(marco4, text="      ")
accel.pack(side=tk.LEFT)

temperatura = tk.Label(marco4, text="Temperatura =")
temperatura.pack(side=tk.LEFT)

temper = tk.Label(marco4, text="      ")
temper.pack(side=tk.LEFT)

hora = tk.Label(marco4, text="Tiempo =")
hora.pack(side=tk.LEFT)

rolex = tk.Label(marco4, text="")
rolex.pack(side=tk.LEFT)

admin = tk.Frame(vent)
admin.pack()

close = tk.Button(admin, width=10, text="CLOSE", command=cl)
close.pack(side=tk.LEFT)


def add_time():
    tiempo = str(int(time()) - tinicial - 1)
    rand = tiempo
    rolex.config(text=rand)
    vent.after(500, add_time)


def sensor2():
    s.send(str.encode("Se."))
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


def sensor():
    s.send(str.encode("Se."))
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

    vent.after(3000, sensor)


vent.after(0, add_time)
vent.after(1000, sensor)
vent.mainloop()
print("se ha cerrado la ventana")

s.close()

texto.close()
