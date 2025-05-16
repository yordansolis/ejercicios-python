"""
Ejercicio 3: Formato de Nombre Completo
Crea una función que reciba nombre y apellido por separado y devuelva el nombre completo formateado (primer letra de cada uno en mayúscula).
"""

def firstName(name, first):
    return (f'Hi, {name.strip().capitalize()} {first.strip().capitalize()}')

    
name =  input('Enter your name: ')
first = input('Enter your first name: ')

response = firstName(name, first)
print(response)
