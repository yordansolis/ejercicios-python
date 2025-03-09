
# Función basica
def saludar():
    print("Hola, soy una función")

# Función con argumentos
def sumar(a, b):
    print(a + b)

# Función con argumentos por defecto
def saludar_persona(nombre="Jhordan"):
    return (f"Hola, {nombre}")


# Función con documentación
def calcular_area(base, altura):
    """
    Calcular el área de un triángulo

    Parámetros:
     base (float): La base del triángulo
     altura (float): La altura del triángulo

    Retorna:
        float: El área del triángulo
    """
    return   (base * altura) / 2

print("1. Función salidar")
saludar()
# print("===========================")
print("2. Función saludar_persona")
resultado = (saludar_persona("Asprilla Solis"))
print(saludar_persona())
print(resultado)

print("===========================")
print("3.Función para calcular el área de un triángulo  return")

areia = (calcular_area(10, 5))
print(areia)
print("===========================")