# Creacion de interfaces graficas: ventanas con las que interactuamos en una pc.
#   Libreria Tkinter
# Formadas por un conjunto de graficos como ventanas, botones, casillas de verificacion, etc.
# GUI: Graphic User Interface
# Librerias con las que trabajar para crear GUI:
# a) Tkinter
# b) WxPython
# c) PyQt
# d) PyGTK

# Formato: Raiz(tk) => Frame => widget (puede ser boton, menu, frames, etc)

import tkinter as tk

def saludar():
    etiqueta.config(text="¡Hola, mundo!")

ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")

etiqueta = tk.Label(ventana, text="Presiona el botón")
etiqueta.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()
