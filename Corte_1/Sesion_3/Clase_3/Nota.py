N=float(input('Ingrese la nota: '))

#if (N>=0 and N<=5): 
if(0<=N<=5):
    if N>=3:
        print('Aprobo')
    else:
        print('reprobo')
else:
    print('La nota ingresada es invalida')