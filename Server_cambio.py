# coding=utf-8
# importamos librerias necesarias
import socket
from serial import *

# variables necesarias para la iniciacion
host = ''
port = 10005
ser = Serial('/dev/ttyACM0', 115200)
dict = { 8 : 'Fwd.' , 5 : 'Sto.',  2: 'Bwd.' , 4:'Let.' , 6:'Rit.'} 

def setup_server():
    """
    setupServe(): None -> socket

    Metodo para iniciar el servidor y unirlo al socket, creando mensajes para mostrar
    el estado de la creacion
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
    try:
        
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print('socket bind complete')
    return s


def setup_connection(s):
    """
    stupConnection(): None -> conn

    

    Metodo para aceptar una conexion de un cliente, devuelve la direccion de la
    conexion
    """
    s.listen(1)  # una sola persona en cualquier momento
    conn, address = s.accept()
    print("Conectado a: " + address[0] + ":" + str(address[1]))
    return conn


def read_serial():
    """
    readSerial(): None -> str

    Metodo que envia el mensaje predeterminado al Arduino para recolectar el
    estado de los sensores, devuelve el valor como un str
    """
    ser.write("Ser.")
    accion = ser.read()
    b = "["
    if accion == "[":
        while accion != "]":
            accion = ser.read()
            b = b + accion
        ser.flush()
    print b
    return b

def dataCompare(data1,data2):
    for i in range(len(data1)):
        if data1[i] != data2[i]:
            if i == 0:
                ser.write(dict[data1])
                


    
def data_transfer(conn):
    """
    dataTransfer(conn): conn -> None

    Metodo que recibe la conexion realizada anterormente e inicializa la comunicacion con la misma, esperando a
    recibir un mensaje, se escribe en el serial el codigo correspondiente para la acción requerida
    """
    # lo que hay aqui recibe y envia datos
    while True:
        # recibo datos
        data_old = ['5',"90","12"]
        data = conn.recv(1024)
        data = data.decode('utf-8')
        data = data.split('/')
        print data
        if data == '':
            ser.write('Sto.')
            print 'Cliente perdido, Cerrando servidor'
            conn.close()
            s.close()
            break 
        else:
            if data != data_old:
                dataCompare(data,data_old)
                read_serial()
                data_old = data
        print "Data has been sent!"


def setup_all():
    """
    Metodo para iniciar el servidor, las conexiones, y el intercambio de mensajes con el cliente
    """
    s = setup_server()
    conn = setup_connection(s)
    data_transfer(conn)


def go():
    """
    Loop principal, donde se realizan todas las acciones
    """
    while True:
        try:
            setup_all()
        except:
            break


go()
