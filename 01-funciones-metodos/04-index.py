def validar_usuario(name, password):
    if name == 'admin' and password == 'admin':
        return True
    return False

def mostrar_bienvenida(nombre):
    print(f"Bienvenido {nombre}")


def mostrar_error():
    print("Usuario o contraseña incorrecta")

def login():
    nombre = input("Ingrese su nombre: ")
    password = input("Ingrese su contraseña: ")

    if validar_usuario(nombre, password):
        mostrar_bienvenida(nombre)
    else:
        mostrar_error()

login() #✅
# Ingrese su nombre: admin
# Ingrese su contraseña: admin
# Bienvenido admin

# login() #✅
# Ingrese su nombre: admin
# Ingrese su contraseña: admin
# Bienvenido admin


# login() #❌
# Ingrese su nombre: jhordan
# Ingrese su contraseña: 123
# Usuario o contraseña incorrecta