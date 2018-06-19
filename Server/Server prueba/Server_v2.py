import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print("bind complete")

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
         print("conexion recibida de" + str(address[0]) + ':' + str(address[1]))
         size = 1024
         while True:
             try:
                 data = client.recv(size)
                 data = data.decode('utf-8')
                 if data:
                     # Set the response to echo back the recieved data
                     print(data)
                     response = data
                     client.send(response)
                 else:
                     raise error('Client disconnected')
             except:
                 client.close()
                 return False

if __name__ == "__main__":
    while True:
        port_num = 5550
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()
