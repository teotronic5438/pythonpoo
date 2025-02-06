'''
Recordamos Tipos de módulos:
    Módulos integrados: Son los que vienen preinstalados con Python (ej.: math, os, sys).
    Módulos externos: Debes instalarlos desde PyPI usando pip (ej.: numpy, pandas).
    Módulos creados por el usuario: Archivos .py que tú mismo defines.

'''

# Ejemplo con módulos integrados
import math
print(math.sqrt(16))  # 4.0


# Importando partes específicas del módulo
# Puedes importar solo lo que necesitas con from ... import.
from math import pi, sqrt
print(pi)        # 3.141592653589793
print(sqrt(25))  # 5.0


# Renombrar un módulo
# Usa la palabra clave as para asignar un alias al módulo.
import math as m
print(m.factorial(5))  # 120


# Creación de un módulo propio

#     Crea un archivo llamado mimodulo.py:

# mimodulo.py
def saludar(nombre):
    return f"Hola, {nombre}!"

    # Úsalo en otro archivo:

import mimodulo
print(mimodulo.saludar("Elias"))  # "Hola, Elias!"



# Instalar y usar un módulo externo (SOLO FUNCIONA SI INSTALAMOS EL PAQUETE, CONSIDERAR EVENT)
#     Instálalo con pip:

# pip install requests

# Úsalo en tu código:

# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)  # 200