def crear_tablero():
    tablero = []
    for f in range(10):
        fila = []
        for c in range(10):
            fila.append(0)
        tablero.append(fila)
    return tablero

def pedir_barcos(tablero):
    while True:
        barco_f = input("Dime la fila: ")
        if barco_f == "":
            break
        barco_f = int(barco_f)
        barco_c = int(input("Dime la columna: "))
        tablero[barco_f][barco_c] = 1

def disparo(tablero):
    print("Ahora las balas")
    objetivo_f = int(input("Dime la fila: "))
    objetivo_c = int(input("Dime la columna: "))

    if tablero[objetivo_f][objetivo_c] == 1:
        print("¡¡¡¡¡TOCADO!!!!!")
    else: 
        print("¡¡¡¡¡AGUA!!!!!")

def main():
    cuadro = crear_tablero()
    pedir_barcos(cuadro)
    disparo(cuadro)

main()