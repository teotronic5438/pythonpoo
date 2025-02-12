# Creacion de interfaces graficas
#   Libreria Tkinter

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
