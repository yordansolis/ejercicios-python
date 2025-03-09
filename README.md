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
