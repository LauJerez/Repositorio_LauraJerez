from factorial import factorial as f
def main():
    n=int(input('Ingrese el numero de elementos: '))
    m=int(input('Ingrese el numero de grupos: '))
    cmb=(f(n)/(f(m)*(f(n-m))))
    print(f'El numero de combinaciones posibles es {cmb}')

if __name__=="__main__":
    main()