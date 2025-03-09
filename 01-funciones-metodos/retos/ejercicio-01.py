"""
Calcular un Descuento
Crea una función que calcule el precio final después de aplicar un descuento. La función debe recibir el precio original y el porcentaje de descuento
"""


def validar_datos(precio, descuento):
    """
    Valida que se hayan proporcionado los dos argumentos y que sean números.
    
    Parámetros:
      precio: El precio del producto.
      descuento: El porcentaje de descuento (en formato decimal).
    
    Retorna:
      bool: True si los datos son válidos, False en caso contrario.
    """
    
    # Verificamos que ningun parametro sea None
    if precio is None or descuento is None:
        return False
    
    if not isinstance(precio, (int, float)) or not isinstance(descuento, (int, float)):
        return False
    
    return True
    

def calcular_descuento(precio, descuento):
    """
    Funcion para calcular el descuento de un producto 
    se reciben 2 argumentos que sera validados por validar_datos
    
    Parametros: 
        Precio: precio del producto original 
        Descuento: porcentaje del descuento ejemplo (15%)
        
    Validación: 
          str: Un mensaje con el precio final o un mensaje de error si los datos no son válidos.
    """
    if not validar_datos(precio, descuento):
        return "Datos Inválidos"
    
    valor_descuento = precio * descuento
    total_descuento = precio - valor_descuento
    
    return f"El precio del articulo con descuento es de {total_descuento}"

print(calcular_descuento(80000, 0.15))