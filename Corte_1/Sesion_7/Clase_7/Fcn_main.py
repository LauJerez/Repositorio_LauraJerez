import Fcn_ext
import Fun3

def main():
    nombre = input('Ingrese su nombre: ')
    surname = input('Ingrese su apellido: ')
    print('------------------------')
    Fcn_ext.matrix(nombre,surname)
    print('------------------------')
    print(f'Ejecutado desde {__name__}')
    print('*************************')
    resultado=Fun3.suma
    print('*************************')


if __name__=="__main__":
    main()