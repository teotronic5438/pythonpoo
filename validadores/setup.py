# desceribe la configuracion del paquete distribuible
from setuptools import setup # type: ignore
setup(
    name="paquete_validador",
    version="1.0",
    description="Validador entero, float, texto, email y contraseña",
    author="Elias Orihuela",
    author_email="elias.orihuela@gmail.com",
    url="https://github.com/teotronic5438",
    packages=["validador"]
)