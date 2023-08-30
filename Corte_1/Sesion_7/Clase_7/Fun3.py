#Funcion sin parametros y sin retorno

def suma():
    a = int(input('Ingrese un número: '))
    b = int(input('Ingrese otro número: '))
    r=a+b
    print(r)
    print(f'Ejecutado desde {__name__}')

if __name__=="__main__":
    print('Inicio de programa')
    
    suma()
    
    print('fin programa')