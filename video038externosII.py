# en modo lectura
archivo_texto = open("ficheros/myfile.txt", "r", encoding="utf-8")
texto = archivo_texto.read()
print(texto)
archivo_texto.close()

# al terminar de leer el archivo el cursor se situa al final
# si precisamos leer el archivo y mover el puntero al inicio, medio o final usamos seek

# en modo lectura
archivo_texto = open("ficheros/myfile.txt", "r", encoding="utf-8")
texto = archivo_texto.read()    # lee el archivo completo

archivo_texto.seek(30)  # mueve el cursor a la posicion 30
texto2 = archivo_texto.read()   # lee el archivo completo desde la posicion 30 marcada por el cursor

archivo_texto.seek(0)   # Mueve el cursor al inicio
texto3 = archivo_texto.read(20) # lee hasta la posicion del puntero indicado (!= a seek)

archivo_texto.close()
# print(texto)
print(texto2)
print(texto3)


# Si quiero leer SOLO LA SEGUNDA MITAD DEL ARCHIVO
archivo_texto = open("ficheros/myfile.txt", "r", encoding="utf-8")

print("\n CIERRA TU PICO\n")
archivo_texto.seek(len(archivo_texto.read())/2)  # mueve el cursor a la mitad de la posicion
print(archivo_texto.read())  # lee el archivo completo desde la segunda mitad


# Abrir el fichero con modo lectura y escritura
archivo_texto = open("ficheros/myfile.txt", "r+", encoding="utf-8") # r+ = lectura y escritura
print(archivo_texto.readlines())
archivo_texto.seek(0)
archivo_texto.write("Hola este es un fichero lectura escitura.\n")
print(archivo_texto.readlines())
