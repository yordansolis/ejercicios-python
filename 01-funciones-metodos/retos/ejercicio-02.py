
"""
Ejercicio 2: Contador de Palabras
Desarrolla una función que reciba un texto y devuelva cuántas palabras contiene.
"""
def validar_datos(texto):
    """
    Valida que se haya proporcionado el argumento str.
    
    Parámetro:
      palabras: El parametro debe ser string.
      descuento: El porcentaje de descuento (en formato decimal).
    
    Retorna:
      bool: True si los datos son válidos, False en caso contrario.
    """
    
    # Verificamos que ningun parametro sea None
    if texto is None:
        return False
    
    if not isinstance(texto, (str)):
        return False
    
    return True
    

def calcular_palabra(texto):
    """
    Funcion para calcular el descuento de un producto 
    se reciben 2 argumentos que sera validados por validar_datos
    
    Parametros: 
        Precio: precio del producto original 
        Descuento: porcentaje del descuento ejemplo (15%)
        
    Validación: 
          str: Un mensaje con el precio final o un mensaje de error si los datos no son válidos.
    """
    if not validar_datos(texto):
        return "Dato Inválido"
        
    
    # Calcular las palabras si todo sale bien
    # Separa el texto en palabras usando split() y cuenta los elementos.
    palabras = texto.split()
    return len(palabras)

print(calcular_palabra("Hola mundo"))
