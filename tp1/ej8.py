'''
Crear una función que reciba una cadena y devuelva True si es un palíndromo.
Recordar que un palíndromo es aquella palabra que, espejada, se sigue leyendo
igual (por ejemplo, neuquen).
'''
def palin(cadena):
    for orig, inv in zip(cadena, reversed(cadena)):
        if orig != inv: return False

def palin2(cadena):
    for orig, inv in zip(range(0, len(cadena)), range(len(cadena)-1, -1, -1)):
        if orig == inv: return True
        if cadena[orig] != cadena[inv]: return False

pal = "neuquen"
print(f"La palabra {pal}: {palin2(pal)}")