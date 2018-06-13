import socket
import RPi.GPIO as GPIO
HOST='192.168.0.106'
PORT=5002
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
GPIO.setmode(GPIO.BCM)
GPIO.setup(02, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
while 1:
    data=s.recv(8096)
    if data=='0':
            print 'Forward'
            GPIO.output(02,True)
            GPIO.output(03, False)
            GPIO.output(11, False)
    elif data=='1':
            print 'Backward'
            GPIO.output(02, False)
            GPIO.output(03, True)
            GPIO.output(11, True)
            GPIO.output(10, False)
    elif data=='2':
            print 'Left'
            GPIO.output(02, False)
            GPIO.output(03, False)
            GPIO.output(11, False)
            GPIO.output(10, True)
    elif data=='3':
            print 'Right'
            GPIO.output(02, True)
            GPIO.output(03, False)
            GPIO.output(11, False)
            GPIO.output(10, False)
    elif data=='5':
            print 'Stop'
            GPIO.output(02, False)
            GPIO.output(03, False)
            GPIO.output(11, False)
            GPIO.output(10, False)
s.close()
