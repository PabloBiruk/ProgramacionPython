# ---- Esto no:

from ctypes.wintypes import WORD


def saluda(nombre):
    print(f"Hola, {nombre}")

saluda(input("Escribe tu nombre: "))

# --------------------------

cadena = "pepito"

def duplicate_encode(word):
    salida = ""
    for l in word.lower():
        contador = word.count(l)
        if contador == 1:
            salida += "("
        else:
            salida += ")"
    return salida

print(duplicate_encode(cadena))

# ---------------------------

#https://cutt.ly/4NDWTy5
