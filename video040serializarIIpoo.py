import pickle

class Vehiculo:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def mostrar_info(self):
        """Muestra la información del vehículo."""
        print(f"Vehículo: {self.marca} {self.modelo}, Año: {self.año}, Color: {self.color}")

    def cambiar_color(self, nuevo_color):
        """Cambia el color del vehículo."""
        self.color = nuevo_color
        print(f"El color ha sido cambiado a {self.color}")

    def es_clasico(self):
        """Determina si el vehículo es clásico (más de 30 años de antigüedad)."""
        return 2024 - self.año > 30

    def encender(self):
        """Simula el encendido del vehículo."""
        print(f"{self.marca} {self.modelo} está encendido.")

# Crear una instancia de la clase Vehiculo
mi_auto = Vehiculo("Toyota", "Corolla", 1990, "Rojo")

# 📌 Guardar el objeto en un archivo binario
with open("ficheros/vehiculo.pkl", "wb") as archivo:
    pickle.dump(mi_auto, archivo)

# 📌 Cargar el objeto desde el archivo binario
with open("ficheros/vehiculo.pkl", "rb") as archivo:
    auto_cargado = pickle.load(archivo)

# Verificar que los datos se han cargado correctamente
auto_cargado.mostrar_info()


# pickle.dump(objeto, archivo_abierto) convierte mi_auto (un objeto de la clase Vehiculo) en bytes y lo guarda en archivo.