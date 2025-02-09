# En Python, un paquete es una forma de organizar y estructurar módulos de código para que sean reutilizables 
# y mantenibles. Un paquete es simplemente un directorio que contiene un archivo especial llamado __init__.py, 
# junto con uno o más módulos de Python.
# 📦 ¿Para qué sirven los paquetes?

# Los paquetes permiten:

#     Organizar código en múltiples archivos y carpetas.
#     Evitar conflictos de nombres al agrupar módulos relacionados.
#     Facilitar la reutilización y distribución del código.
#     Permitir importaciones jerárquicas (import paquete.subpaquete.modulo).

# Son directorios donde se almacenaran modulos relacionados entre si.

# Para que una carpeta funcion como paquete debe tener un archivo __init__.py

#    carpeta_paquete.modulo (si hay clases usamos sus nombres o  * y traemos todo)
'''
from calculos.calculos_generales import division

division(10, 2)

from calculos.calculos_generales import *

redondear(10.2)
sumar(2,3)
restar(10,2)
multiplicar(10,2)
division(4,5)
potencia(3,4)
'''

# Ahora agregamos calculos y paquetes añadidos
from calculos.basicos.basicos import *
sumar(5,7)

