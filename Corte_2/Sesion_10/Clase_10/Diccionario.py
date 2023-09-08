festivo = {
    'Enero':['1 - año nuevo','6-Reyes magos'],
    'Febrero':['no tiene festivos'],
    'Marzo':[' 20- Dia de San Jose']}

def main():
    mes = input('Ingrese un mes: ')
    print(festivo[mes])

if __name__=="__main__":
    main()