class Coche():
    def desplazamiento(self):
        print("El coche se mueve usando 4 ruedas.")

class Moto():
    def desplazamiento(self):
        print("La moto se mueve usando 2 ruedas.")
        
class Camion():
    def desplazamiento(self):
        print("El camión se mueve usando 8 ruedas.")

# miMoto = Moto()
# miMoto.desplazamiento()

# miAuto = Coche()    
# miAuto.desplazamiento()

# miCamion = Camion()
# miCamion.desplazamiento()

# usamos polimorfismo, para que sepa a que metodo llamar
# es debilmente tipado, no es necesario especificar el tipo
def desplazamientoVehiculos(vehiculo):
    vehiculo.desplazamiento()

# instancio un objeto    
# miVehiculo = Moto()
# miVehiculo = Coche()
miVehiculo = Camion()

#uso polimorfismo
desplazamientoVehiculos(miVehiculo)