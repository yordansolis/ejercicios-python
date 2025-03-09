# Ejercicios-python

Ejercicios y logica de programación

# 1. Retos de funciones y metodos

Las funciones son bloques de código reotilizables que realizan una tera específica. Son fundamentables en programación porque permiten dividir problemas complejos en partes más pequeñas y manejables.

## Que es una función ?

Una función es un bloque de código con un nombre que puede ser "llamado" (ejecutado) en diferentes partes de un programa.

## Porque utilizarlas ?

- Reutulización de codigo.
- Modelaridad.
- Mantenibilidad.
- Legilibilidad.

Ejemplo:
01-funciones-metodos

<hr>

### Diferencias entre `return` y `print()` en Python:

**`return`:**

- Devuelve un valor desde una función.
- Permite utilizar el valor devuelto posteriormente en el programa.
- Finaliza la ejecución de la función al ejecutarse.

**Ejemplo:**

```python
def sumar(a, b):
    return a + b

resultado = sumar(2, 3)
print(resultado)  # Salida: 5

```

**`print`:**

- Solo Muestra información en pantalla.
- No devuelve un valor que pueda ser reutilizado posteriormente (devuelve None).

**Ejemplo:**

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

resultado = saludar("Ana")
print(resultado)  # Salida: None

```

<hr>

## Las funciones son adeacuadas para:

1.  operaciones repetitivas

**Ejemplo:**

```python
def calcular_iva(monto):
    return monto * 0.19

precio_producto1= 1000
precio_producto2= 2000

print("1. Calcular IVA")
print(calcular_iva(precio_producto1)) #✅ 190.0
print(calcular_iva(precio_producto2)) #✅ 380.0
```

2. Para organizar el código por funcionalidad

**Ejemplo:**

```python
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


<hr>
```
