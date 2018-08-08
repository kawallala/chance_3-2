from turtle import*


def mapeo(nombre,y,z):
    archivo = open(nombre, 'r')
    to = 0
    for line in archivo:
      line = line[1:len(line)-2]
      line = line.split('/')
      estado = line[1]
      #temperatura = float(line[2])
      #temperatura = temperatua * 0.48828125 * 10 // 10
      vel = float(line[3])
      dt = 10 * (float(line[4]) - to)
      to = float(line[4])
      if estado == '8':
        fd(vel * dt)
      if estado == '4':
        lt(vel * dt * 90 / 17.7)
      if estado == '6':
        rt(vel * dt * 90 / 17.7)
      if estado == '2':
        bd(vel * dt)
        
        
