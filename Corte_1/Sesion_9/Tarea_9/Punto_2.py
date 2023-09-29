# Punto 2:
from random import randint as r

def encontrar(lista):
    if len(lista) == 1:
        return lista[0]
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def main():
    Lista = [r(1, 50) for _ in range(15)]
    print("La lista es:", Lista)
    maximo_lista = encontrar(Lista)
    print("El numero maximo en la lista es:", maximo_lista)

if __name__ == "__main__":
    main()