# Función sencilla para calcular la distancia entre dos puntos
def calcular_distancia(punto1, punto2):
    # Extraemos las coordenadas de cada punto
    x1, y1 = punto1
    x2, y2 = punto2
    
    # Calculamos la diferencia en cada eje
    diferencia_x = x2 - x1
    diferencia_y = y2 - y1
    
    # Usamos la fórmula de la distancia euclidiana
    distancia = (diferencia_x**2 + diferencia_y**2) ** 0.5
    return distancia

# Ejemplo 1:
punto_a = (2, 3)
punto_b = (5, 5)
print("Ejemplo 1 - Distancia entre", punto_a, "y", punto_b, "es:", calcular_distancia(punto_a, punto_b))
# Resultado: 3.605551275463989

print("===========================")

# Ejemplo 2:
punto_c = (3, 4)
punto_d = (6, 8)
print("Ejemplo 2 - Distancia entre", punto_c, "y", punto_d, "es:", calcular_distancia(punto_c, punto_d))
# Resultado: 5.0
"""


"""