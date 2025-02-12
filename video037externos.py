# Archivos externos
# Objetivo: persistencia de datos
# Se puede hacer de dos formas: archivos externos o BBDD.

# Fases para manejar archivos externos

# CREACION => APERTURA => MANIPULACION => CIERRE

# El módulo io provee las facilidades principales de Python para manejar diferentes tipos de E/S. Hay tres
#  diferentes tipos de E/S: texto E/S, binario E/S e E/S sin formato. Estas son categorías generales y varios 
# respaldos de almacenamiento se pueden usar para cada una de ellas. Un objeto concreto perteneciendo a cualquiera 
# de estas categorías se llama un file object. Otros términos comunes son stream y file-like object.

# en modo escritura
archivo_texto = open("ficheros/myfile.txt", "w", encoding="utf-8")

frase = "Aprendiendo el uso de ficheros.\nHoy es sabado por la noche 2.\n"

archivo_texto.write(frase)

archivo_texto.close()

# en modo lectura
archivo_texto = open("ficheros/myfile.txt", "r", encoding="utf-8")
texto = archivo_texto.read()
archivo_texto.seek(0)  # Mueve el cursor al inicio
texto_lineas = archivo_texto.readlines()
archivo_texto.close()
print(texto)
print(texto_lineas)

print()

# otra opcion de lectura, el with asegura apertura y cierre del archivo
with open("ficheros/myfile.txt", "r", encoding="utf-8") as archivo_texto:
    for linea in archivo_texto:
        print(linea.strip())  # Eliminamos saltos de línea extra


# agregando texto al archivo MODO=append (extension añadir)
archivo_texto = open("ficheros/myfile.txt", "a", encoding="utf-8")
archivo_texto.write("Esta es una nueva linea.\n")
archivo_texto.close()
