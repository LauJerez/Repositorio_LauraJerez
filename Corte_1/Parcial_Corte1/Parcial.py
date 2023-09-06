import random as r

def rates():
    comision = r.randint(10,50)
    return comision

def menu():
    print('Seleccione una de las diguientes opciones: \n'\
          '1. Conversion de COP a la divisa seleccionada\n'\
            '2. Ver las tasas de cambio y su correspondiante comision')
    

def main():
    menu()
    comision=rates()
    sel=input('Ingrese una de las opciones: ')
    if (sel=='1') or (sel=='Conversion de COP a la divisa seleccionada'):
        print('USD,EUR,CNY,JPY,PEN')
        div = input('A que divisa desea convertir: ')
        COP = input('Cuantos COP desea cambiar: ')
        
        if (div.lower()=='USD'):
            USD = 4108
            Precio_venta = USD+(USD*{comision})
            print(Precio_venta)
            
        elif (div.lower()=='EUR'):
            EUR = 4454
            Precio_venta = EUR+(EUR*{comision})
            print(Precio_venta)
        elif (div.lower()=='CNY'):
            CNY = 563
            Precio_venta = CNY+(CNY*{comision})
            print(Precio_venta)
        elif (div.lower()=='JYP'):
            JYP = 28
            Precio_venta = JYP+(JYP*{comision})
            print(Precio_venta)
        elif (div.lower()=='PEN'):
            PEN = 1106
            Precio_venta = PEN+(PEN*{comision})
            print(Precio_venta)

    elif (sel=='2') or (sel=='Ver las tasas de cambio y su correspondiante comision'):
        print(f'Divisa: USD, Tasa: 4108, Comision: {comision} \n'\
              f'Divisa: EUR, Tasa: 4454, Comision: {comision}\n'\
                f'Divisa: CNY, Tasa: 563, Comision: {comision}\n'\
                    f'Divisa: JPY, Tasa: 28, Comision: {comision}\n'\
                        f'Divisa: PEN, Tasa: 1106, Comision: {comision}')
    else:
        print('Seleccion invalida')


if __name__=="__main__":
    main()