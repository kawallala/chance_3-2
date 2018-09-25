import matplotlib.pyplot as plt
import numpy as np

nombre = raw_input('Que archivo quiere abrir? ')
datos = open(nombre, 'r')

pos = []
accx = []
accy = []
accz = []
T = []
t = []
i = 0
for line in datos:
    if i > 50:
        line = line[1:len(line)-2]
        line = line.split('/')
        pos.append(line[1])
        acceleraciones = line[0].split(';')
        acceleraciones[0] = -0.15 * int(acceleraciones[0]) + 52
        acceleraciones[1] = -0.15 * int(acceleraciones[1]) + 50.01
        acceleraciones[2] = -0.14 * int(acceleraciones[2]) + 47.7
        accx.append(acceleraciones[0])
        accy.append(acceleraciones[1])
        accz.append(acceleraciones[2])
        T.append(float(line[2])* 0.48828125 * 10 // 10)
        t.append(float(line[3]))
    i+=1
maxacc=max([max(accx), max(accy), max(accz)])
minacc=min([min(accx), min(accy), min(accz)])
tmin = min(t)
tmax= max(t)



plt.figure(1,figsize=(6,3))
plt.subplot(121)
plt.axis((tmin,tmax,maxacc,minacc))
plt.plot(t , accx)
plt.plot(t , accy)
plt.plot(t , accz)
plt.xlabel('Tiempo [s]')
plt.ylabel('acceleraciones por eje [m/s^2]')
plt.title('Aceleraciones')
plt.subplot(122)
plt.axis((tmin,tmax,10,20))
plt.plot(t,T)
plt.xlabel('Tiempo[s]')
plt.ylabel('Temperatura [C]')
plt.title('Temperaturas')
plt.show()
