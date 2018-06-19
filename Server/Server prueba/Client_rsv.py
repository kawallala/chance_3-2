import socket
import Tkinter as tk
host = '172.29.1.1'
port = 5550

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = raw_input("Enter your command: ")
    if command == 'EXIT':   #enviar los datos
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply= s.recv(1024)
    print(reply.decode('utf-8'))
