# probando paquete distribuido e instalado

# from validadores.validadores import *
from validadores.validadores.validadores import validar_entero

validar_entero()

# NOTA: tuve que usar tres validadores. porque el primero tambien tenia __init__.py y lo tomo
# como un paquete tambien, si no lo habria puesto quedaria:
# from validadores.validadores import validar_entero