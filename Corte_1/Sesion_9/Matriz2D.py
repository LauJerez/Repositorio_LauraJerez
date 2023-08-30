# i representa filas y j columnas

def main(Filas, Columnas):
    matriz = []
    for i in range(Filas):
        matriz.append([])
        for j in range(Columnas):
            num = int(input(f'Ingrese el numero de posicion [{i},{j}]: '))
            matriz[i].append(num)
    for i in matriz:
        print(i)
    # return matriz

if __name__=="__main__":
    Filas=int(input('Ingrese el numero de filas: '))
    Columnas=int(input('Ingrese el numero de columnas: '))
    print(main(Filas,Columnas))