from PIL import Image
import Tkinter as tk

im = Image.open("flecha.png")

vent = tk.Tk()


holi = tk.Label(Image=im)
holi.pack()
