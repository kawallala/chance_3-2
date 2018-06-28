import socket
from Tkinter import*
from time import*

tinicial= int(time())

host = '172.30.1.1'
port = 10003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


def divide(x):
    r = x.split('/')
    return r


def element1(x):
    r = x[1:len(x)]
    return r


def element2(x,c):
    r = x[c]
    return r


def element3(x):
    r = x[0:len(x)-1]
    return r


def xyz(sting):
    r = sting.split(';')
    r1 = r[0] + 'X'
    r2 = r[1] + 'Y'
    r3 = r[2] + 'Z'
    r = r1 + '-' + r2 + '-' + r3
    return r

def fd():
    s.send(str.encode("Fd."))
    return


def left():
    s.send(str.encode("Lf."))
    return
  

def staph():
    s.send(str.encode("St."))
    return
  

def right():
    s.send(str.encode("Rt."))
    return
  

def bd():
    s.send(str.encode("Bd."))
    vent.destroy()
    return


def cl():
    s.send(str.encode("CLOSE"))
    vent.destroy()
    return


def kl():
    s.send(str.encode("KILL"))
    vent.destroy()
    return


nombre = raw_input("Ingrese el nombre del archivo donde guardara sus datos")


texto = open(nombre, 'w')

vent = Tk()


def sd():
    vent.destroy()


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

kill = Button(admin, width=10, text="KILL", command=kl)
kill.pack(side=LEFT)

shut_down = Button(admin, width=10, text="SHUT DOWN", command=sd)
shut_down.pack()


def add_time():
  tiempo = str( int(time()) - tinicial -1)
  rand = tiempo
  rolex.config(text=rand)
  vent.after(500, add_time)


def sensor():
  s.send(str.encode("Se."))
  men = s.recv(1024)

  texto.write(men + '\n')

  data = divide(men)
  
  acce = element2(data, 0)
  acce = element1(acce)
  acce = xyz(acce)

  accel.config(text=str(acce))
  
  estado = element2(data,1)
  
  temp = element2(data,2)
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
