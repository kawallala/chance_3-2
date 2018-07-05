import socket
from Tkinter import*
from time import*

# Declaracion de todas las variables usadas mas adelante en el programa


# Momento en que empieza a correr el programa para saber cuanto tiempo lleva corriendo
tinicial = int(time())

# Network de ZeroTier
ZeroTier = '88503383909a8fc4'

# direccion IP del host del server y el numero de puerto usado
host = '192.168.43.46'
port = 10003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# ## -------------------------------------------------------------------------------------------------------------- ## #

# Funciones de procesamiento de datos

# Divide el arreglo de datos por /, para separar aceleracion estado y temperatura


def agregar(x):
    m = x[0:len(x)-1] + '/' + str(time()) + "]"
    return m


def divide(x):
    r = x.split('/')
    return r


# Devuelve el arreglo sacandole el primer elemento

def element1(x):
    r = x[1:len(x)]
    return r


# Entrega el elemento c, en este caso lo utilizamos para sacar el primer elemento

def element2(x,c):
    r = x[c]
    return r


# Devuelve el arregl, pero sin el primer elemento

def element3(x):
    r = x[0:len(x)-1]
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
    return


# Abrimos este archivo de texto para guardar todos los

nombre = raw_input("Ingrese el nombre del archivo donde guardara sus datos")


texto = open(nombre, 'w')


# ###--------------------------------------------------------------------------------------------------------------### #

# Esta seccion es toda la programacion referente a la ventana de python


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
marco4.pack()


acelerometro = Label(marco4, text="Acelerometro =" )
acelerometro.pack(side=LEFT)

accel = Label(marco4, text="      ")
accel.pack(side=LEFT)

temperatura = Label(marco4, text="Temperatura =" )
temperatura.pack(side=LEFT)

temper = Label(marco4,text="      ")
temper.pack(side=LEFT)

hora = Label(marco4, text="Tiempo =" )
hora.pack(side=LEFT)

rolex = Label(marco4, text="")
rolex.pack(side=LEFT)

admin = Frame(vent)
admin.pack()

close = Button(admin, width=10, text="CLOSE", command=cl)
close.pack(side=LEFT)


def add_time():
  tiempo = str( int(time()) - tinicial -1)
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
    temp = int(temp)*0.48828125*10//10
    temper.config(text=str(temp)+'C')
  
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
