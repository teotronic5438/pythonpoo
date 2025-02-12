# 🔍 ¿Qué es la serialización en Python?

# La serialización es el proceso de convertir un objeto de Python en un formato que pueda almacenarse o
#  transmitirse, como JSON, pickle o XML, para luego reconstruirlo más tarde (deserialización).

# 📌 Ejemplo práctico: Guardar un diccionario en un archivo y luego recuperarlo.

# Guardar en un fichero externo unca coleccion, un diccionario o un objeto.
# Se puede codificar en codigo binario, objetivo: distribuir objeto construido en python.

# EL primer caso sera el binario: para esto usaremos la biblioteca Pickle
# De esta biblioteca usaremos los metodos dump() y load().

# Guardaremos en un fichero externo una lista de nombres
import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel", "Elias", "Agus", "Miriam", "Anais", "Leticia"]

fichero_binario = open("ficheros/lista_nombtres", "wb")

pickle.dump(lista_nombres, fichero_binario)
# pickle.dump(datos_a_guardar, archivo_donde_se_guardara)
fichero_binario.close()

del(fichero_binario)


# Ahora hacemos el proceso inverso, leemos archivo binario, lo cargamos en una variable y lo imprimimos.
fichero_texto = open("ficheros/lista_nombtres", "rb")
lista = pickle.load(fichero_texto)
print(lista)