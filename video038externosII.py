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