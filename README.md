# Ejercicios-python

Ejercicios y lógica de programación

# 1. Retos de funciones y métodos

Las funciones son bloques de código reutilizables que realizan una tarea específica. Son fundamentales en programación porque permiten dividir problemas complejos en partes más pequeñas y manejables.

## ¿Qué es una función?

Una función es un bloque de código con un nombre que puede ser "llamado" (ejecutado) en diferentes partes de un programa.

## ¿Por qué utilizarlas?

- Reutilización de código.
- Modularidad.
- Mantenibilidad.
- Legibilidad.

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

## Las funciones son adecuadas para:

### 1. Operaciones repetitivas

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

### 2. Para organizar el código por funcionalidad

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

```

### 3. Para abstraer operaciones complejas

**Ejemplo:**

```python

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

```

### 4. Para crear operaciones con efectos secundarios controlados

**Ejemplos:**

```python
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
```

# Conclusión

- Cada función debería hacer una sola cosa y hacerla bien.
- Usar nombres que describan lo que hace la función.
- Incluya como parámetros solo los que necesite trabajar.
- Las funciones deberían ser relativamente pequeñas (10-20 líneas de código).
- Documentar las funciones para que se explique el propósito, parámetros y valores de retorno.
- Manejar bien los errores.

---

## Concurrencia y async / await

### ¿Cuándo usar async/await?

✅ Usa `async def` cuando:

- Haces llamadas a bases de datos con drivers asíncronos (asyncpg, motor, databases)
- Llamas APIs externas con httpx.AsyncClient o aiohttp
- Usas librerías async como aiofiles, redis.asyncio

### ❌ NO uses async def cuando:

- Usas ORMs síncronos (SQLAlchemy sin async, Django ORM)
- Haces operaciones CPU-intensivas (cálculos pesados, procesamiento de imágenes)
- Usas librerías bloqueantes (requests, pymongo, psycopg2)

### Comparación práctica

❌ Incorrecto (async con código síncrono)

```python
import requests

@app.get("/users")
async def get_users():
    # ¡MAL! requests es bloqueante
    response = requests.get("https://api.example.com/users")
    return response.json()
```

✅ Correcto (async con httpx)

```python
import httpx

@app.get("/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/users")
        return response.json()
```

✅ Correcto (sync si usas requests)

```python
import requests

@app.get("/users")
def get_users():  # Sin async
    response = requests.get("https://api.example.com/users")
    return response.json()
```

### Diagrama de decisión

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  ¿Tu función ESPERA algo externo?                  │
│  (base de datos, API, archivo, red)                │
│                                                     │
│           SÍ ────────► usa async def                │
│                                                     │
│           NO ────────► usa def                      │
│                                                     │
└─────────────────────────────────────────────────────┘

        ┌─────────────────────┐
        │   Tu endpoint       │
        └──────────┬──────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ ¿Llamas a algo       │
        │ que tarda tiempo?    │
        └──────┬───────────────┘
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
    ┌──────┐        ┌──────┐
    │  SÍ  │        │  NO  │
    └──┬───┘        └───┬──┘
       │                │
       ▼                ▼
  ┌─────────────┐  ┌──────────┐
  │ ¿La librería│  │  usa def │
  │ es async?   │  │          │
  └──┬──────────┘  └──────────┘
     │
  ┌──┴───┐
  │      │
  ▼      ▼
┌────┐ ┌────┐
│SÍ  │ │NO  │
└─┬──┘ └─┬──┘
  │      │
  ▼      ▼
async   def
 def
```

---

# Usando uv con FastAPI

Para usar uv con esta aplicación, dentro del directorio del proyecto ejecuta:

```bash
uv init --app
```

```bash
uv add fastapi --extra standard
```

Para ejecutar la aplicación FastAPI:

```bash
uv run fastapi dev
```

Docs: https://docs.astral.sh/uv/guides/integration/fastapi/#migrating-an-existing-fastapi-project
