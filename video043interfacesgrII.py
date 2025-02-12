from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x400")
root.title("Segundo GUI - Frame")
# Crear un Frame con tamaño 400x300 y color de fondo
frm = Frame(root, bg="#7ca7fe", width=400, height=300)
frm.grid()

# Evitar que el Frame se colapse al ajustar los widgets
frm.grid_propagate(False)

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()
