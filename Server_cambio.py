# coding=utf-8
# importamos librerias necesarias
import socket
from serial import *

# variables necesarias para la iniciacion
host = ''
port = 10000
ser = Serial('/dev/ttyACM0', 115200)
dict = { 8 : 'Fwd.' , 5 : 'Sto.',  2: 'Bwd.' , 4:'Let.' , 6:'Rit.'} 
data_old = ['5',"90","12"]

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
    return b

def dataCompare(data1,data2):
    for i in range(len(data1)):
        if data1[i] != data2[i]:
            if i == 0:
                if data1[i] == '8':
                    ser.write('Fwd.')
                    print 'avanzando'
                elif data1[i] == '4':
                    ser.write('Lef.')
                    print 'izquierda'
                elif data1[i] == '6':
                    ser.write('Rit.')
                    print 'derecha'
                elif data1[i] == '5':
                    ser.write('Sto.')
                    print ' detenido'
                elif data1[i] == '2':
                    ser.write('Bwd.')
                    print 'retrocediendo'
            elif i == 1:
                a = int(data1[1])/10
                print 'c' + str(a) + '.'
                ser.write('c' + str(a) + '.')
            elif i == 2:
                print 'v' + data1[2] + '.'
                ser.write('v' + data1[2] + '.')
                


    
def data_transfer(conn):
    """
    dataTransfer(conn): conn -> None

    Metodo que recibe la conexion realizada anterormente e inicializa la comunicacion con la misma, esperando a
    recibir un mensaje, se escribe en el serial el codigo correspondiente para la acción requerida
    """
    # lo que hay aqui recibe y envia datos
    while True:
        global data_old
        # recibo datos
        data = conn.recv(1024)
        data = data.split('/')
        #print data
        if data == ['']:
            ser.write('Sto.')
            print 'Cliente perdido, Cerrando servidor'
            conn.close()
            s.close()
            break
        elif data == ['CLOSE']:
            ser.write('Sto.')
            print 'Cliente desconectado, Cerrando servidor'
            conn.close()
            s.close()
            break
        else:
            dataCompare(data,data_old)
            a=read_serial()
            #print a
            conn.sendall(a)                       
            data_old = data
        print "Data Sent"


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
