# coding=utf-8
# importamos librerias necesarias
import socket
from serial import *

# variables necesarias para la iniciacion
host = ''
port = 10006
ser = Serial('/dev/ttyACM0', 115200)


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


def data_transfer(conn):
    """
    dataTransfer(conn): conn -> None

    Metodo que recibe la conexion realizada anterormente e inicializa la comunicacion con la misma, esperando a
    recibir un mensaje, se escribe en el serial el codigo correspondiente para la acción requerida
    """
    # lo que hay aqui recibe y envia datos
    while True:
        # recibo datos
        data = conn.recv(1024)
        data = data.decode('utf-8')
        data = data[:4]
        print data
        if data == '':
            ser.write('Sto.')
            print 'Cliente perdido, Cerrando servidor'
            conn.close()
            s.close()
            break
        elif data == 'Fwd.':
            ser.write('Fwd.')
        elif data == 'Lef.':
            ser.write('Lef.')
        elif data == 'Rit.':
            ser.write('Rit.')
        elif data == 'Sto.':
            ser.write('Sto.')
        elif data == 'Bwd.':
            ser.write('Bwd.')
        elif data == 'Ser.':
            datos = read_serial()
            conn.sendall(str.encode(datos))
        elif data[0]=='v' and len(data) == 4:
            print 'Cambiando la velocidad'
            ser.write(data)
        elif data == 'CLOSE':
            ser.write('Sto.')
            print 'Cliente desconectado, Cerrando servidor'
            conn.close()
            s.close()
            break
        else:
            print 'Comando no reconocido'
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
