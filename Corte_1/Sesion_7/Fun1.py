#Funcion con parametros y retorno

def suma(a,b):
    resultado=a+b
    return resultado


print('Inicio del programa')
a=int(input('Ingrese un número: '))
b=int(input('Ingrese otro número: '))
resultado=suma(a,b)
print(resultado)
print('Fin del programa')