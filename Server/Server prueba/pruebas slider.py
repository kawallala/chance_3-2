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
port = 10004

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


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
    s.send(str.encode("Fwd."))
    state.config(text="Avanzando")
    return sensor2()


def leftt():
    s.send(str.encode("Lef."))
    state.config(text="Izquierda")
    return sensor2()


def staph():
    s.send(str.encode("Sto."))
    state.config(text="Detenido")
    return sensor2()


def right():
    s.send(str.encode("Rit."))
    state.config(text="Derecha")
    return sensor2()


def bd():
    s.send(str.encode("Bwd."))
    state.config(text="Retrocediendo")
    return sensor2()


def fast():
    s.send(str.encode("v25."))
    return


def mids():
    s.send(str.encode("v18."))
    return


def slow():
    s.send(str.encode("v15."))
    return


def speed(event):
    print fast.get()
    return

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


marco1 = Tk.Frame(vent)
marco1.pack()

fddr = Tk.Label(marco1, width=15)
fddr.pack(side=Tk.LEFT)

fd = Tk.Button(marco1, width=100, image=Fup, command=fd)
fd.pack(side=Tk.LEFT)

fdiz = Tk.Label(marco1, width=5)
fdiz.pack(side=Tk.LEFT)

marco11 = Tk.Frame(marco1)
marco11.pack()

marco12 = Tk.Frame(marco1)
marco12.pack()

marco13 = Tk.Frame(marco1)
marco13.pack()

fast = Tk.Scale(marco11, from_=12, to=24, command=speed)
fast.set(100)
fast.pack(side=Tk.LEFT)

marco2 = Tk.Frame(vent)
marco2.pack()

left = Tk.Button(marco2, width=100, image=Flf, command=right)
left.pack(side=Tk.LEFT)

stop = Tk.Button(marco2, width=100, image=Fst, command=staph)
stop.pack(side=Tk.LEFT)

right = Tk.Button(marco2, width=100, image=Frt, command=leftt)
right.pack(side=Tk.LEFT)

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


def add_time():
    tiempo = str(int(time()) - tinicial - 1)
    rand = tiempo
    rolex.config(text=rand)
    vent.after(500, add_time)


def sensor2():
    s.send(str.encode("Ser."))
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
    s.send(str.encode("Ser."))
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
