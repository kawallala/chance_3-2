import socket

HOST='192.168.43.46'
PORT=5002
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
    data=s.recv(8096)
    if data=='0':
            print 'Forward'
            s.sendto('holi', ( HOST , PORT ) )

    elif data=='1':
            print 'Backward'
            
    elif data=='2':
            print 'Left'
            
    elif data=='3':
            print 'Right'
            
    elif data=='5':
            print 'Stop'
            
s.close()
