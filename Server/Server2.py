import RPi.GPIO as GPIO
import socket
HOST='192.168.43.46'
PORT=5002
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr=s.accept()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
print 'Connected by', addr
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
while True:
    a = conn.recv(1024)
    if a == "Fd.":
        print(1)
s.close()
