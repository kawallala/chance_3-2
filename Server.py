import socket
from serial import *
import sys

host = ''
port = 10003
ser = Serial('/dev/ttyACM1', 115200)
storedValue = 'what up'

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print('socket bind complete')
    return s

def setupConnection(s):
    s.listen(2) #una sola persona en cualquier momento
    conn, address = s.accept()
    print("Conectado a: " + address[0] + ":" + str(address[1]))
    return conn

def readSerial():
     ser.write("Se.")
     accion = ser.read()
     b = "["
     if accion == "[":
          while accion != "]":
               accion= ser.read()
               b = b + accion
          ser.flush()
     print (b)
     return b


def dataTransfer(conn):
    #lo que hay aqui recibe y envia datos
    while True:
        #recibo datos
        data = conn.recv(1024)
        data = data.decode('utf-8')
        print(data)
        if data == '':
            print 'Cerrando servidor'
            conn.close()
            s.close()
            break
        elif data == 'Fd.':
            ser.write('Fd.')
        elif data == 'Lf.':
            ser.write('Lf.')
        elif data == 'Rt.':
            ser.write('Rt.')
        elif data == 'St.':
            ser.write('St.')
        elif data == 'Bd.':
            ser.write('Bd.')
        elif data == 'Se.':
            datos = readSerial()
            conn.sendall(str.encode(datos))
        elif data == 'CLOSE':
            print 'Cliente desconectado'
            conn.close()
            s.close()
        #separamos los datos, para separar el comando del resto de los datos
        print("Data has been sent!")

s = setupServer()

while True:
    try:
        conn = setupConnection(s)
        dataTransfer(conn)
    except:
        conn.close()
        s.close()
        sys.exit()
        break

