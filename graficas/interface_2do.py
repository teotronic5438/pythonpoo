from tkinter import *

raiz = Tk()

raiz.title("Primer GUI")
# raiz.resizable(True, True) 
# admite boolenos (width, height) si va 0 no permite redimensionar

# raiz.iconbitmap("nombre_archivo.ico") # con esto cambio icono

raiz.geometry("600x400")    # redimensiona la ventna

raiz.config(bg="#7ca7fe")   # modifica el color de fondo de la ventana

miFrame = Frame()
miFrame.pack(side="left", anchor="n")
miFrame.config(bg="red")
miFrame.config(width="600", height="400")
# comportamiento por defecto queda anclado

# el metodo mainloop siempre debe ir al final
raiz.mainloop() # ventana en bucle infinito pero debe estar a la escucha de eventos