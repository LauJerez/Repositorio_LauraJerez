
# Para poder abrir un archivo en python usar el comando: f=open(<NombreDelArchivo>,'rt')
# f.close() Para cerrarlo

def lectura():
    f = open('matrizAsignacion.txt','rt')
    line = f.readlines() #f.readlines() lee todo el texto
    f.close()
    for i in line:
        a=i.rstrip('\n').split(',')
        print(f'{a} => {int(a[0])+int(a[1])}') #Suma las dos primeras posiciones


def lectura2():
    f = open('matrizAsignacion.txt','rt')
    line = f.readline() #f.readline() lee una linea del texto
    # f.seek(<posicion a la que desea mover>) me va amostrar los valores desde donde esta ubicado el puntero
    while line!='':
        print(line)
        opc = input('presione enter') 
        line = f.readline()
    f.close()
    print('Finalizo la lectura')


def lectura3():
    f = open('matrizAsignacion.txt','rt')
    line = f.read()
    f.close()
    print(line)
    print('------------------------------')
    a=line.split('\n')
    for i in a:
        b=i.split(',')
        print(b)

def main():
    lectura()
    lectura2()
    lectura3()

if __name__=="__main__":
    main()