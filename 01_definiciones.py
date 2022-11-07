
def hola():
    print("Hola")

def saludo(nombre,dia):
    print(f"Buenas tardes, {nombre}. Hoy es {dia}")

saludo("Teo","Lunes")

#-------------------------

def inversa(cadena):
    return cadena[::-1]

palabras = ["uno","dos","tres","cuatro"]

for p in palabras:
    x = inversa("Hola")
    print(x)

#------------------------

def cuenta_vocales(cadena):
    vocales = {}
    letras = "aeiou"

    for c in letras:
        vocales[c] = cadena.lower().count(c)

    return vocales

texto = "ASODKPAOSDKPAOSdkpoaksdpoaksdpOKAPSODKAPOSDKAPosdk askdpoakpsdoaks dpoKPA OSdkpOAksdpaod aposk dpaos"

x = cuenta_vocales(texto)
print(x)

#-----------------------

def suma(a,b):
    return a + b 

resultado = suma(1,2)
print(resultado)

#-----------------------

def censura(cadena):
    inicio = "*" * (len(cadena) - 4)
    final = cadena[-4:]
    return inicio + final

texto = "pos"
x = censura(texto)
print(x)


# --------------------

def contiene_letra(cadena,letra):
    return letra in cadena


a = "a"