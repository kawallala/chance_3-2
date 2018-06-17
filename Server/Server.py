import socket 
import sys
PORT_NUMBER = 5000
SIZE = 1024
hostName = socket.gethostbyname( '0.0.0.0' )
mySocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
mySocket.bind((hostName, PORT_NUMBER))
mySocket.listen(1)
conn, addr = mySocket.accept()
print("Test server listening on port {0}\n".format(PORT_NUMBER))
print("connected by", addr)
while True:
     (data,addr) = mySocket.recvfrom(SIZE)
     print(data)
sys.ext()

