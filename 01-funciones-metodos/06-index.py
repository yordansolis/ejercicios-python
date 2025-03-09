usuarios = []

def agregar_usuario(nombre, edad):
    usuarios.append({"nombre": nombre, "edad": edad})
    return usuarios

def listar_usuarios():

    if not usuarios:
        return "No hay usuarios registrados"
    
    print("Lista de usuarios")
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")


agregar_usuario("Jhordan", 25)
agregar_usuario("Andres", 30)
listar_usuarios()
# Lista de usuarios
# Nombre: Jhordan, Edad: 25
# Nombre: Andres, Edad: 30
print("===========================")
agregar_usuario("Salome", 20)
listar_usuarios()
# Lista de usuarios
# Nombre: Jhordan, Edad: 25
# Nombre: Andres, Edad: 30
# Nombre: Salome, Edad: 20
print("===========================")