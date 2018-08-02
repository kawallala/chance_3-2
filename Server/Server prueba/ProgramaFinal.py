import socket
import Tkinter as Tk
import time
from PIL import Image, ImageTk

# ### ------------------------------------------------------------------------------------### #

# En esta seccion del codigo estan escritas todas las constantes usadas más abajo

# el momento en el que se ejecuto el programa
tinicial = int(time.time())

# La direccion ip del servidor y el puerto usado para la coneccion servidor-cliente (raspberry-nosotros)
host = '192.168.42.46'
port = 10005

# El socket creado para la conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

# Estos son los 3 parametros que le dicen a la raspberry como actuar, siendo estado el si avanza, se detiene
# gira o retrocede, cam es el angulo de la camara entre -90 y 90 y vel el voltaje aplicado a los motores
#del robot siendo 12 el minimo y 24 el maximo
estado = 5
cam = 0
vel = 12

# El nombre del archivo donde se van a guarddar todos los datos recopilados por el robot 
nombre = raw_input("Ingrese el nombre del archivo donde guardara sus datos: ")

# Se abre el archivo
texto = open(nombre, 'w')

# ### ------------------------------------------------------------------------------------### #

# None -> None
# Las 5 siguientes funciones sirven para manejar el robot, lo hacen avanzar
# girar a la izquierda, detenerse, girar a la derecha y retroceder respectivamente

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

# None -> None
# Esta funcion sirve para cerrar la ventana y terminar el servidor que esta corriendo en la 
# raspberry

def cl():
    s.send(str.encode("CLOSE"))
    vent.destroy()
    return

# None -> None
# Esta funcion cambia el parametro vel, que representa el voltaje que se le envian a los motores,
# para cambiar la velocidad de estos

def speed(event):
    global vel
    a = str(fast.get())
    vel = a
    return

# None -> None
# Esta funcion modifica el parametro cam, que representa los grados a los cuales se posiciona el
# servomotor que sostiene la camara

def camara(event):
    global cam
    a = str(fast1.get())
    cam = a
    return


# ### ------------------------------------------------------------------------------------### #

# Esta parte son todas las partes que conforman a nuestra Interfaz grafica 


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

# ### ------------------------------------------------------------------------------------### #


# None -> None
# Esta funcion modifica el label rolex en nuestra interfaz, que representa cuanto tiempo ha
# pasado desde que se abrio la interfaz.

def add_time():
    tiempo = str(int(time()) - tinicial - 1)
    rolex.config(text=tiempo)
    vent.after(500, add_time)

# None -> None
# Esta funcion le envia a la raspberry los parametros estado, cam y vel repectivamente ,
# despues espera a recibir la informacion de los sensores y la muestra dentro de nuestra 
# interfaz modificando los labels accel (aceleracion del robot), temper (temperatura en
# donde esta el robot) y estado (si esta avanzando , detenido, etc...)
# Ademas esta funcion se repite cada 0.1 segundos

def sensor():
    global estado,cam,vel
    print str(estado) + '/' + str(cam) + '/' + str(vel)
    message = str(estado) + '/' + str(cam) + '/' + str(vel)
    s.send(str.encode(message))
    men = s.recv(1024)

    texto.write(men + '\n')

    data = men.split(':')

    acceleration = data[0].split('/')
    acceleration = acceleration[0] + acceleration[1]+ acceleration[2]
    accel.config(text=str(acceleration))

    estado = data[1]

    temp = data[3]
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
