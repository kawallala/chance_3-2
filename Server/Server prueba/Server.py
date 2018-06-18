import socket

host = ''
port = 5500

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

def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]

def dataTransfer(conn):
    #lo que hay aqui recibe y envia datos
    while True:
        #recibo datos
        data = conn.recv(1024)
        data = data.decode('utf-8')
        #separamos los datos, para separar el comando del resto de los datos
        dataMessage = data.split(' ',1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("our client has left us")
            break
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        else:
            reply = 'Unknown Comannd'
        #enviar la respuesta
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection(s)
        dataTransfer(conn)
    except:
        break

