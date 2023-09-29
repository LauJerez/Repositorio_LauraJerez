# Punto 1:
from random import randint as r

def crear_matriz():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(10):
            num = r(1, 50)
            matriz[i].append(num)
    return matriz

def imprimir(matriz):
    for fila in matriz:
        print(fila)

def max_min(matriz):
    menor = mayor = matriz[0][0]
    posc_mayor = (0, 0)
    posc_menor = (0, 0)

    for i, fila in enumerate(matriz):
        for j, numero in enumerate(fila):
            if numero < menor:
                menor = numero
                posc_menor = (i, j)
            elif numero > mayor:
                mayor = numero
                posc_mayor = (i, j)

    print(f"\nEl número mayor de la  matriz es {mayor} y esta en la posición {posc_mayor}\n")
    print(f"El número menor de  la matriz es {menor} y esta en la posición {posc_menor}")


def organizar(matriz):
    lista_matriz = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista_matriz.append(matriz[i][j])
            lista_matriz.sort(reverse=True)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = lista_matriz.pop(0)
        print(matriz[i])


def main():
    matriz = crear_matriz()
    print("Matriz original:")
    imprimir(matriz)
    max_min(matriz)

    print("\nMatriz ordenada de mayor a menor:")
    organizar(matriz)

if __name__ == "__main__":
    main()