from serial import*


ser = Serial('/dev/ttyACM1', 9600)

a = ""
while 1:
     
     r= ser.read()
     if r == '[':
          a = ""
     if r == ']':
          print( a +']'
                 )
          
     a += r
