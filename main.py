
import math
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API REST Calculadora")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],  # Permitir todos los encabezados
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)


# Modelo de datos para operaciones POST
class Operacion(BaseModel):
    a: float
    b: float

# ----------------------------
# GET con parámetros en la URL
# ----------------------------
@app.get("/sumar", status_code=status.HTTP_200_OK)
def sumar(a: float, b: float):
    """
    Suma dos números enviados como parámetros en la URL.
    Ejemplo: /sumar?a=2&b=3
    """
    return {"resultado": a + b}

@app.get("/restar", status_code=status.HTTP_200_OK)
def restar(a: float, b: float):
    """Resta dos números enviados como parámetros."""
    return {"resultado": a - b}

@app.get("/factorial", status_code=status.HTTP_200_OK)
def factorial(n: int):
    """Calcular el factorial de un numero"""
    fact=1
    for i in range (1, n+1):
        fact=fact*i
    return {"resultado": fact}
# ----------------------------
# POST con cuerpo JSON
# ----------------------------
@app.post("/multiplicar", status_code=status.HTTP_201_CREATED)
def multiplicar(datos: Operacion):
    """Multiplica dos números enviados en el cuerpo JSON."""
    return {"resultado": datos.a * datos.b}

@app.post("/dividir", status_code=status.HTTP_200_OK)
def dividir(datos: Operacion):
    """Divide dos números, validando la división entre cero."""
    if datos.b == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede dividir entre cero"
        )
    return {"resultado": datos.a / datos.b}

@app.post("/potencia", status_code=status.HTTP_200_OK)
def potencia(datos: Operacion):
    """Calcula la potencia de a elevado a b (a^b)"""
    return {"resultado": datos.a ** datos.b}

@app.post("/modulo", status_code=status.HTTP_200_OK)
def mod(datos: Operacion):
    """Calcula el modulo de a % b"""
    if datos.b == 0:
      raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede dividir entre cero"
        )
    return {"resultado": datos.a % datos.b}

@app.post("/logaritmo", status_code=status.HTTP_200_OK)
def log(datos: Operacion):
    """Calcula el logaritmo de 'a' en base 'b'"""
    if datos.a <= 0:
      raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="a debe ser mayor que 0"
        )
    if datos.b <= 0 or datos.b == 1:
       raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="b debe ser mayor que 0 o diferente de 1"
       )
    return {"resultado": math.log(datos.a, datos.b)}
