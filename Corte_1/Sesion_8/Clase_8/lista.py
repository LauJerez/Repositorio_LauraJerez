
def agregar(milista):
    num=int(input('Qe desea agregar: '))
    milista.append(num)
    print(milista)

def main(milista):
    opc=''
    while opc!='exit':
        print('seleccione una opcion:\n',\
            '1. Append')

        opc=input('seleccion: ')
        
        if opc=='1':
            agregar(milista)

if __name__=="__main__":
    milista=[2,3,4]
    main(milista)