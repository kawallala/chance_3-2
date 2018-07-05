import socket
import thread
from serial import *

class SocketServer(socket.socket):
     clients = []
     ser = Serial('/dev/ttyACM0',115200)    
     def __init__(self):
          socket.socket.__init__(self)
          #To silence- address occupied!!
          self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
          self.bind(('', 10003))
          self.listen(5)
          

     def run(self):
          print "Server started"
          try:
               self.accept_clients()
          except Exception as ex:
               print ex
          finally:
               print "Server closed"
               for client in self.clients:
                    client.close()
               self.close()

     def accept_clients(self):
          while 1:
               (clientsocket, address) = self.accept()
               #Adding client to clients list
               self.clients.append(clientsocket)
               #Client Connected
               self.onopen(clientsocket)
               #Receiving data from client
               thread.start_new_thread(self.recieve, (clientsocket,))

     def recieve(self, client):
          while 1:
               data = client.recv(1024)
               data = data.decode('utf-8')
               print data
               if data == '' or data== 'CLOSE':
                    break
               elif data == 'Fd.':
                    self.ser.write('Fd.')
               elif data == 'Lf.':
                    self.ser.write('Lf.')
               elif data == 'Rt.':
                    self.ser.write('Rt.')
               elif data == 'St.':
                    self.ser.write('St.')
               elif data == 'Bd.':
                    self.ser.write('Bd.')
               elif data == 'Se.':
                    datos = self.readSerial()
                    datos = str.encode(datos)
               #Message Received
               self.onmessage(client, datos)
          #Removing client from clients list
          self.clients.remove(client)
          #Client Disconnected
          self.onclose(client)
          #Closing connection with client
          client.close()
          #Closing thread
          thread.exit()
          print self.clients

     def broadcast(self, message, client):
          #Sending message to all clients
          client.send(message)
               
     def readSerial(self):
          self.ser.write("Se.")
          accion = self.ser.read()
          b="["
          if accion == "[":
               while accion != "]":
                    accion = self.ser.read()
                    b += accion
               self.ser.flush()
          print b
          return b

     def onopen(self, client):
          pass

     def onmessage(self, client, message):
          pass
 
     def onclose(self, client):
         pass

class ArduinoServer(SocketServer):

    def __init__(self):
        SocketServer.__init__(self)

    def onmessage(self, client, message):
        print "Client Sent Message"
        #Sending message to all clients
        self.broadcast(message, client)

    def onopen(self, client):
        print "Client Connected"

    def onclose(self, client):
        print "Client Disconnected"

def main():
    server = ArduinoServer()
    server.run()

if __name__ == "__main__":
    main()
