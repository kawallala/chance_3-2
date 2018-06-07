from serial import*
from time import *



ser = Serial('/dev/ttyACM0', 115200)
T_inicial = int(time())

print ("bienvenido al robot chance_3-2")
print ("que desea hacer?")
print ("Avanzar = W")
print ("Retroceder = X")
print ("Derecha = D")
print ("Detener = S")

while 1:     
     a = raw_input("Que desea hacer?")
     if a == "W":
          ser.write("Fd.")
     elif a == "X":
          ser.write("Bd.")
     ser.write("Se.")
     accion = ser.read()
     b = "["
     if accion == "[":
          while accion != "]":
               accion= ser.read()
               b = b + accion
     print (b)
     
     
