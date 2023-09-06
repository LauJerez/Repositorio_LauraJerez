from random import uniform as u

def rates():
    comision=[]
    for i in range(5):
        comision.append(round(u(0.1,0.5),2))
    # print(comision)
    return comision


def ver_tasas(comision,divisas,cambios):
    for i in range(5):
        print(f'Divisa: {divisas[i]}, Tasa: {cambios[i]}, Comisión: {comision[i]}')

def conversion(comision,divisas,cambios):
    div=input('A que divisa desea hacer el cambio: ').upper()
    if div in divisas:
        idx=divisas.index(div)
        divisa=divisas[idx]
        tasa=int(cambios[idx])
        comisiones=comision[idx]
        Precio_venta=tasa+(tasa*comisiones)
        cambio=int(input('Que valor desea cambiar: '))
        total= cambio//Precio_venta # // Parte entera de una division ejem. 44.52 queda 44
        vueltas=round((cambio - Precio_venta*total),2)
        print(f'Cambio: {total} {divisa}, Devolucion: {vueltas} COP')
        return 1
    print('Ingrese un valor valido\n')



def menu():
    comision=rates()
    divisas=['USD','EUR','CNY','JPY','PEN']
    cambios=['4108','4454','563 ','28  ','1106']
    print(' 1. Conversion de COP a la divisa seleccionada\n','2. Ver las tasas de cambio y su correspondiante comision\n','3. salir\n')
    opc=input('Ingrese una de las opciones: ')
    
    while opc!='salir':
        if opc=='1':
            conversion(comision,divisas,cambios)
        elif opc=='2':
            ver_tasas(comision,divisas,cambios)
        elif opc=='salir' or '3':
            break
        else:
            print('Seleccion invalida')
        print('1. Conversion de COP a la divisa seleccionada\n','2. Ver las tasas de cambio y su correspondiante comision\n','3. salir\n')
        opc=input('Ingrese una de las opciones: ')

def inicio():
    menu()



if __name__=="__main__":
    inicio()