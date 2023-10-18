def iva(producto, neto, porcentaje_iva):
    valor_iva = (neto * porcentaje_iva) / 100
    v_base = neto + valor_iva
    return v_base, valor_iva

def canasta(producto, neto):
    alimentos = {
        'cr_porciento': ['Arroz', 'pan', 'otros productos de panaderia', 'papa', 'yuca', 'otros tuberculos', 'platano',
                            'cebolla', 'tomate', 'zanahoria', 'revuelto verde', 'Otras hortalizas y legumbres frescas',
                            'Frijol', 'Arveja', 'Otras hortalizas y legumbres secas', 'naranjas', 'bananos',
                            'tomate de arbol', 'Moras', 'Otras frutas frescas', 'Res', 'Cerdo', 'Pollo',
                            'Pescado de mar rio y enlatado', 'Huevos', 'Leche', 'Queso', 'Panela', 'Sal', 'Agua',
                            'Almuerzo', 'Hamburguesa', 'Comidas rapidas calientes', 'Gastos de cafeteria',
                            'Comidas rapidas frias'],
        'cin_porciento': ['Harina de maiz y otras harinas', 'Pastas alimenticias', 'Otros cereales',
                            'Carnes frias y embutidos', 'Azucar', 'Cafe', 'Chocolate'],
        'dcnv_porciento': ['Cereales preparados', 'Hortalizas y legumbres enlatadas',
                                 'Frutas en conserva o secas', 'Otros productos de mar', 'Otros derivados lacteos',
                                 'Aceites', 'Grasas', 'Otros condimentos', 'Sopas y cremas', 'Salsas y aderezos',
                                 'Dulces confites y gelatinas', 'Otros abarrotes']}
    if producto in alimentos['cr_porciento']:
        return neto, 0
    elif producto in alimentos['cin_porciento']:
        v_base, valor_iva = iva(producto, neto, 5)
        return v_base, valor_iva
    elif producto in alimentos['dcnv_porciento']:
        v_base, valor_iva = iva(producto, neto, 19)
        return v_base, valor_iva
    else:
        return 'Error, intente nuevamente'

def main():
    while True:
        producto = input('Ingrese el nombre del producto o si desea finalizar (escriba la palabra "salir"): ')
        if producto.lower() == 'salir':
            break

        neto = float(input('Ingrese el valor neto del producto: '))

        rslt = tuple(canasta(producto, neto))

        if rslt:
            v_base, valor_iva = rslt
            print(f'Valor Base: {round(v_base, 2)}')
            print(f'Valor IVA: {round(valor_iva, 2)}\n')
        else:
            print(rslt)

if __name__ == "__main__":
    main()