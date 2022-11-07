def precio_entrada():
    print("Consulte el precio de sus entradas al Zoológico")
    edades = []

    while True:
        entrada = input("Introduzca las edades de los visitantes: ")
        if entrada == '':
            break
        else:
            ent=int(entrada)
            edades.append(ent)

    suma = 0

    for e in edades:
        if e <= 2:
            suma = suma
        elif e <= 12:
            suma += 14.00
        elif e <= 65:
            suma += 23.00
        else:
            suma += 18.00
    return print(suma)


print(precio_entrada())