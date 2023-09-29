# Punto 3:

def posiciones(a, b):
    psc = []
    for i in range(len(a)):
        if a[i] == b:
            psc.append(i)
    return psc

def main():
    a = str(input('Ingrese una palabra: '))
    b = str(input('Ingrese una letra de esa palabra: '))
    psc = posiciones(a, b)

    if not psc:
        print(f"la letra '{b}' no se encuentra en la palabra '{a}'")
    else:
        print(f"Las posiciones de '{b}' en '{a}' son: {psc}")

if __name__ == "__main__":
    main()