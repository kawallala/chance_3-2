import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP = '192.168.43.46'
PORT_NUMBER = 5000
SIZE = 1024
print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )

while True:
     mySocket.sendto( 'cool',(SERVER_IP,POT_NUMBER))
sys.ext()
