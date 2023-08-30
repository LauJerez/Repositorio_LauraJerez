from random import randint as r

def crear_matriz(Filas, Columnas):
    matriz = []
    for i in range(Filas):
        matriz.append([])
        for j in range(Columnas):
            #num = int(input(f'Ingrese el numero de posicion [{i},{j}]: '))
            num=r(1,10)
            matriz[i].append(num)
    return matriz

def imprimir(matriz):
    for i in matriz:
        print(i)

def escalar(matriz):
    n=int(input('Ingrese el escalar: '))
    for i in matriz:
        for j in range(len(i)):
            i[j]=n*i[j]   # i en valor de j
    imprimir(matriz)

def main():
    matriz=crear_matriz(Filas,Columnas)
    imprimir(matriz)
    escalar(matriz)


if __name__=="__main__":
    Filas=int(input('Ingrese el numero de filas: '))
    Columnas=int(input('Ingrese el numero de columnas: '))
    main()