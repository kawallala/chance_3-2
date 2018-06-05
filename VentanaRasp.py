from Tkinter import*
from comandos import*


ventana = Tk("Robot Explorador", "hola", "Robot Explorador")

m1 = Frame(ventana)
m1.pack()


forward = Button(m1, width=20, text="Adelante", command=adelante)
forward.pack(side=LEFT)

### -------------------------------------------------------------------------------------------------------------###

m2 = Frame(ventana)
m2.pack()

left = Button(m2, width=20, text="Izquierda", command=izquierda)
left.pack(side=LEFT)


stop = Button(m2, width=20, text="Detenerse", command=parar)
stop.pack(side=LEFT)

right = Button(m2, width=20, text="Derecha", command=derecha)
right.pack(side=LEFT)

### -------------------------------------------------------------------------------------------------------------###

m3 = Frame(ventana)
m3.pack()

backward = Button(m3, width=20, text="Retroceder", command=retroceder)
backward.pack(side=LEFT)


ventana.mainloop()
