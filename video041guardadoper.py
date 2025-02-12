# USaremos un fichero para ir guardando paulativamente
# util para reutilizar en el futuro.
'''

import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"Se ha creado una persona con el nuevo nombre: {self.nombre}")
    
    def __str__(self):
        return(f"Nombre: {self.nombre}. Genero: {self.genero}. Edad: {self.edad}.")

class ListaPersonas:
    personas =[]

    def agregarPersonas(self, p):
        self.personas.append(p)
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

miListaPersonas = ListaPersonas()

per = Persona("Sandra", "femenino", 23)
miListaPersonas.agregarPersonas(per)

per = Persona("Juan", "Masculino", 18)
miListaPersonas.agregarPersonas(per)

per = Persona("Lucia", "femenino", 28)
miListaPersonas.agregarPersonas(per)

miListaPersonas.mostrarPersonas()

'''

import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"Se ha creado una persona con el nombre: {self.nombre}")
    
    def __str__(self):
        return f"Nombre: {self.nombre}. Género: {self.genero}. Edad: {self.edad}."

class ListaPersonas:
    def __init__(self):
        # Intentar cargar los datos desde el archivo binario al iniciar
        self.personas = self.cargarDesdeArchivo()

    def agregarPersona(self, p):
        self.personas.append(p)
        self.guardarEnArchivo()  # Guardar automáticamente después de agregar

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarEnArchivo(self):
        """Guarda la lista de personas en un archivo binario"""
        with open("ficheros/personas.pkl", "wb") as archivo:
            pickle.dump(self.personas, archivo)

    def cargarDesdeArchivo(self):
        """Carga la lista de personas desde el archivo binario (si existe)"""
        try:
            with open("ficheros/personas.pkl", "rb") as archivo:
                return pickle.load(archivo)
        except (FileNotFoundError, EOFError):  # Si el archivo no existe o está vacío
            return []

# ✅ Crear la lista de personas (carga desde el archivo)
miListaPersonas = ListaPersonas()

# ✅ Agregar nuevas personas
per1 = Persona("Sandra", "Femenino", 23)
miListaPersonas.agregarPersona(per1)

per2 = Persona("Juan", "Masculino", 18)
miListaPersonas.agregarPersona(per2)

per3 = Persona("Lucía", "Femenino", 28)
miListaPersonas.agregarPersona(per3)

# ✅ Mostrar todas las personas (incluidas las cargadas del archivo)
print("\n📌 Lista de personas almacenadas:")
miListaPersonas.mostrarPersonas()
