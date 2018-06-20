from serial import*
from time import *

def mostrar_sensores():
     #sleep(delay)
     ser.write("Se.")
     accion = ser.read()
     b = "["
     if accion == "[":
          while accion != "]":
               accion= ser.read()
               b = b + accion
          ser.flush()
     print (b)

ser = Serial('/dev/ttyACM0', 115200)
T_inicial = int(time())
sensores = True

print ("bienvenido al robot chance_3-2")
print ("que desea hacer?")
print ("Avanzar = W")
print ("Retroceder = X")
print ("Derecha = D")
print ("Detener = S")

while 1:
     Start= raw_input("Desea activar los sensores? Y/n ")
     if Start == "Y":
          sensores = True
          break
     elif Start == "n":
          sensores = False
          break
     else:
          print ("comando no reconocido")

while 1:     
     a = raw_input("Que desea hacer? ")
     if a == "W":
          ser.write('Fd.')
     elif a == "X":
          ser.write('Bd.')
     elif a == "A":
          ser.write('Lf.')
     elif a == "D":
          ser.write('Rt.')
     elif a== "S":
          ser.write('St.')     
     else:
          print("escriba un comando de la lista")
          continue
     if sensores:
          mostrar_sensores()
     
     
