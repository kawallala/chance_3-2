import matplotlib.pyplot as plt
import numpy as np

nombre = raw_input('Que archivo quiere abrir? ')
datos = open(nombre, 'r')

pos = []
accx = []
accy = []
accz = []
t = [t for t in range(3192)]
T = []

for line in datos:
    line = line[1:len(line)-2]
    line = line.split('/')

    pos.append(line[1])
    acceleraciones = line[0].split(';')
    accx.append(acceleraciones[0])
    accy.append(acceleraciones[1])
    accz.append(acceleraciones[2])
    T.append(line[2])

plt.plot(t,accx)
plt.plot(t,accy)
plt.plot(t,accz)
plt.xlabel('Tiempo [s]')
plt.ylabel('acceleracion eje x [m/s^2]')
plt.show()
