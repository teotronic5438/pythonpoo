import re

def validar_entero():
    """Solicita un número entero hasta que sea válido."""
    while True:
        dato = input("Ingrese un número entero: ")
        try:
            valor = int(dato)
            return valor
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")

def validar_flotante():
    """Solicita un número flotante hasta que sea válido."""
    while True:
        dato = input("Ingrese un número flotante: ")
        try:
            valor = float(dato)
            return valor
        except ValueError:
            print("❌ Error: Debe ingresar un número flotante válido.")

def validar_texto():
    """Solicita un texto no vacío hasta que sea válido."""
    while True:
        dato = input("Ingrese un texto: ").strip()
        if dato:
            return dato
        print("❌ Error: El texto no puede estar vacío.")

def validar_correo():
    """Solicita un correo válido hasta que sea correcto."""
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        dato = input("Ingrese un correo electrónico: ").strip()
        if re.match(patron, dato):
            return dato
        print("❌ Error: Correo inválido. Debe tener el formato usuario@dominio.com")

def validar_password():
    """Solicita una contraseña válida (6-15 caracteres, mayúscula, minúscula y número)."""
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,15}$'
    while True:
        dato = input("Ingrese una contraseña (6-15 caracteres, al menos una mayúscula, una minúscula y un número): ")
        if re.match(patron, dato):
            return dato
        print("❌ Error: La contraseña debe tener entre 6 y 15 caracteres, incluir al menos una mayúscula, una minúscula y un número.")

# 🔍 Ejecución de pruebas
if __name__ == "__main__":
    print("\nValidaciones de usuario:")
    entero = validar_entero()
    flotante = validar_flotante()
    texto = validar_texto()
    correo = validar_correo()
    password = validar_password()

    print("\n✅ Datos ingresados correctamente:")
    print(f"Entero: {entero}")
    print(f"Flotante: {flotante}")
    print(f"Texto: {texto}")
    print(f"Correo: {correo}")
    print(f"Contraseña: {'*' * len(password)} (oculto por seguridad)")
