# metodos de las cadenas (como manipularlas como objetos)
'''
upper()= Devuelve una cadena con todas las letras en mayúsculas.
lower()= Devuelve una cadena con todas las letras en minusculas.
capital()= Devuelve una cadena con la primer letra en Mayúscula.
count() = Cuenta cuantas veces aparece una letra o cadena de caracteres en una fras o string.
find()= Devuelve el indice o posicion en la cual aparece un caracter o grupo de caracteres en una frase.
isdigit()= Devuelve true o false si el valor introducido es numerido o no.
isalum()= Devuelve true  o false si el valor introducido es alphanumerico
isalpha()= Devuelve true o false si el valor introducido es solo letras
split()= separa por palabras utiizando espacios
'''

# strip()
# Elimina los espacios en blanco al inicio y al final de una cadena.

texto = "  hola mundo  "
print(texto.strip())  # "hola mundo"

# lower()
# Convierte todos los caracteres a minúsculas.

texto = "Hola Mundo"
print(texto.lower())  # "hola mundo"

# upper()
# Convierte todos los caracteres a mayúsculas.

texto = "Hola Mundo"
print(texto.upper())  # "HOLA MUNDO"

# replace()
# Reemplaza una subcadena por otra.

texto = "Hola Mundo"
print(texto.replace("Hola", "Adiós"))  # "Adiós Mundo"

# split()
# Divide la cadena en una lista usando un separador.

texto = "manzana,banana,cereza"
print(texto.split(","))  # ["manzana", "banana", "cereza"]

# join()
# Une elementos de una lista en una sola cadena, usando un separador.

lista = ["manzana", "banana", "cereza"]
print(", ".join(lista))  # "manzana, banana, cereza"

# startswith()
# Verifica si la cadena comienza con una subcadena específica.

texto = "Hola Mundo"
print(texto.startswith("Hola"))  # True

# endswith()
# Verifica si la cadena termina con una subcadena específica.

texto = "Hola Mundo"
print(texto.endswith("Mundo"))  # True

# find()
# Devuelve la posición de la primera aparición de una subcadena, o -1 si no se encuentra.

texto = "Hola Mundo"
print(texto.find("Mundo"))  # 5

# count()
# Cuenta cuántas veces aparece una subcadena.

texto = "Hola Hola Mundo"
print(texto.count("Hola"))  # 2

# isnumeric()
# Verifica si todos los caracteres son numéricos.

texto = "12345"
print(texto.isnumeric())  # True

# capitalize()
# Convierte el primer carácter en mayúscula y el resto en minúsculas.

texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"


# isdigit()
# Verifica si todos los caracteres de la cadena son dígitos (números).

texto = "12345"
print(texto.isdigit())  # True
texto = "123a"
print(texto.isdigit())  # False

# isalnum()
# Verifica si todos los caracteres son alfanuméricos (letras y/o números, sin símbolos ni espacios).

texto = "Python123"
print(texto.isalnum())  # True
texto = "Python 123"
print(texto.isalnum())  # False

# isalpha()
# Verifica si todos los caracteres son letras (sin números ni símbolos).

texto = "Python"
print(texto.isalpha())  # True
texto = "Python123"
print(texto.isalpha())  # False

# replace()
# Reemplaza una subcadena por otra en la cadena.

texto = "Hola Mundo"
print(texto.replace("Mundo", "Python"))  # "Hola Python"

# rfind()
# Devuelve la posición de la última aparición de una subcadena. Si no se encuentra, devuelve -1.

texto = "Hola Mundo, Hola Python"
print(texto.rfind("Hola"))  # 13
print(texto.rfind("Adiós"))  # -1