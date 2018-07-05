#importamos librerias necesarias
import socket
from serial import *

#variables necesarias para la iniciacion
host = ''
port = 10003
ser = Serial('/dev/ttyACM0', 115200)

def setupServer():
    '''
    setupServe(): None -> socket

    Metodo para iniciar el servidor y unirlo al socket, creando mensajes para mostrar
    el estado de la creacion
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print('socket bind complete')
    return s

def setupConnection(s):
    '''
    stupConnection(): None -> conn

    Metodo para aceptar una conexion de un cliente, devuelve la direccion de la
    conexion
    '''
    s.listen(1) #una sola persona en cualquier momento
    conn, address = s.accept()
    print("Conectado a: " + address[0] + ":" + str(address[1]))
    return conn

def readSerial():
    '''
    readSerial(): None -> str

    Metodo que envia el mensaje predeterminado al Arduino para recolectar el
    estado de los sensores, devuelve el valor como un str
    '''
    ser.write("Se.")
    accion = ser.read()
    b = "["
    if accion == "[":
        while accion != "]":
            accion= ser.read()
            b = b + accion
        ser.flush()
    print b
    return b


def dataTransfer(conn):
    '''
    dataTransfer(conn): conn -> None

    Metodo que recibe la conexion realizada anterormente e inicializa la comunicacion con la misma, esperando a recibir un mensaje, se escribe
    en el serial el codigo correspondiente para la acción requerida
    '''
    #lo que hay aqui recibe y envia datos
    while True:
        #recibo datos
        data = conn.recv(1024)
        data = data.decode('utf-8')
        print data
        if data == '':
            print 'Cliente perdido, Cerrando servidor'
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
            print 'Cliente desconectado, Cerrando servidor'
            conn.close()
            s.close()
            break
        print("Data has been sent!")

def setupAll():
    '''
    Metodo para iniciar el servidor, las conexiones, y el intercambio de mensajes con el cliente
    '''
    s = setupServer()
    conn = setupConnection(s)
    dataTransfer(conn)

def go():
    '''
    Loop principal, donde se realizan todas las acciones
    '''
    while True:
        try:
            setupAll()
        except:
            break
    
go()

