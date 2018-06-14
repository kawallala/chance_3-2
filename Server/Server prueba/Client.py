import socket

host = '192.168.0.23'
port = 5060

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter your command: ")
    if command == 'EXIT':   #enviar los datos
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply= s.recv(1024)
    print(reply.decode('utf-8'))
s.close()