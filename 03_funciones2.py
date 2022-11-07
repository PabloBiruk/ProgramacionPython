def encadenar(separador,*args):
    """
    Concatena las cadenas contenidas en args y las separa con el separador
    """
    return separador.join(args)

palabras = []

while True:
    entrada = input("Dime una palabra: ")
    if entrada == "":
        break
    else:
        palabras.append(entrada)

sep = input("Dime un separador: ")

print(encadenar("---",*palabras))