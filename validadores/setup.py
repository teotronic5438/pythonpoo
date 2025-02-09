# desceribe la configuracion del paquete distribuible
from setuptools import setup, find_packages # type: ignore

setup(
    name="paquete_validador",
    version="1.0",
    description="Validador entero, float, texto, email y contraseña",
    author="Elias Orihuela",
    author_email="elias.orihuela@gmail.com",
    url="https://github.com/teotronic5438",
    packages=find_packages(),
    install_requires=[],
)

# cuando estamos en la carpeta que esta este archivo corremos el siguiente comando:

# python setup.py sdist

# pip install setuptools    # si no tenemos instalado setuptools

# una vez creada la carpeta dist, entro a ese directorio y vere el paquete que puedo compartir
# se lo paso a otro compañero y ejecuto el comando para instalarlo

# pip3 install nombre_paquete (si escribo las dos primeras letras + tab aparece)