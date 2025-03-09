
# Función basica
def saludar():
    return ("Hola, soy una función")

# Función con argumentos
def sumar(a, b):
    return a + b

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
    return (base * altura) / 2

print("1. Función salidar")
print(saludar())
print("===========================")
print("2. Función saludar_persona")
print(saludar_persona())
print(saludar_persona("Salome"))
print("===========================")
print("3.Función para calcular el área de un triángulo")
print(calcular_area(10, 5))
print("===========================")