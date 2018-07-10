from PIL import Image, ImageTk
import Tkinter as tk

root = tk.Tk()

img = Image.open("Fdw.png")

tkimage = ImageTk.PhotoImage(img)

imge = Image.open("Fup.png")
Fup = ImageTk.PhotoImage(imge)

foto = tk.Frame(root)
foto.pack(side=tk.LEFT)

izq = tk.Label(foto, image=tkimage)
izq.pack(side=tk.LEFT)
der = tk.Label(foto, image=Fup)
der.pack(side=tk.LEFT)

root.mainloop()


img = Image.open("Fup.png")
Fup = ImageTk.PhotoImage(img)

imge = Image.open("Fdw.png")
Fdw = ImageTk.PhotoImage(imge)

imgr = Image.open("Flf.png")
Flf = ImageTk.PhotoImage(imgr)

imgt = Image.open("Frt.png")
Frt = ImageTk.PhotoImage(imgt)
