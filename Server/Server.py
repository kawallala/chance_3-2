from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT_NUMBER = 5000
SIZE = 1024
CLIENT_IP = '192.168.43.154'

hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
     (data,addr) = mySocket.recvfrom(SIZE)
     #mySocket.sendall(bytes('hola'),'utf-8')
     print data
     
sys.ext()

