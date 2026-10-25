import random

LISTA_PALABRAS = [
    "PYTHON",
    "PROGRAMACION",
    "AHORCADO",
    "COMPUTADOR",
    "DESARROLLO",
    "ALGORITMO",
    "VARIABLES",
    "FUNCION",
    "TECNOLOGIA",
    "UNIVERSIDAD"
]

def obtener_palabra_aleatoria():
    """Selecciona y retorna una palabra aleatoria de la lista en mayúsculas."""
    return random.choice(LISTA_PALABRAS)