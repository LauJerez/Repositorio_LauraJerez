#IMC: Personas ya dadas
class Imc:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.estatura = None
        self.peso = None

    def calculo(self):
        imc = self.peso / ((self.estatura / 100) ** 2)
        return imc

    def tabla_de_imc(self, imc):
        if imc < 18.5:
            return "Por debajo"
        elif 18.5 <= imc < 24.9:
            return "Estádo saludable"
        elif 25 <= imc < 29.9:
            return " Sobrepeso"
        elif 30 <= imc < 34.9:
            return " obesidad I"
        elif 35 <= imc < 39.9:
            return "obesidad II"
        elif imc >= 40:
            return "obesidad III"
        else:
            return "Error"

def main():
    persona1 = Imc()
    persona1.nombre = 'Pedro'
    persona1.apellido = 'Caceres'
    persona1.estatura = 188
    persona1.peso = 97

    persona2 = Imc()
    persona2.nombre = 'Maria'
    persona2.apellido = 'Perez'
    persona2.estatura = 160
    persona2.peso = 47

    persona3 = Imc()
    persona3.nombre = 'Julian'
    persona3.apellido = 'Dominguez'
    persona3.estatura = 158
    persona3.peso = 58

    persona4 = Imc()
    persona4.nombre = 'Jessica'
    persona4.apellido = 'Fuentes'
    persona4.estatura = 170
    persona4.peso = 73

    personas = [persona1,persona2, persona3, persona4]
    for persona in personas:
        imc = persona.calculo()
        resultado_imc = persona.tabla_de_imc(imc)
        print(f'La persona: {persona.nombre} {persona.apellido}, \n'\
              f'peso: {persona.peso} kg, \n'\
              f'altura: {persona.estatura} cm, \n'\
              f'tiene un IMC: {round(imc, 1)},\n'\
              f'y se encuentra en:{resultado_imc}\n')

if __name__ == "__main__":
    main()

#IMC: Agregar Persona o No agregarla.
class Imc:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.estatura = None
        self.peso = None


    def calculo(self):
        imc = self.peso / ((self.estatura / 100) ** 2)
        return imc

    def tbl_imc(self, imc):
        if imc < 18.5:
            return "Por debajo"
        elif 18.5 <= imc < 24.9:
            return "Estádo saludable"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidad I"
        elif 35 <= imc < 39.9:
            return "Obesidad II"
        elif imc >= 40:
            return "Obesidad III"
        else:
            return "Error"

def main():
    Personas = []
    opc = 'y'
    while opc != 'n':
        per = Imc()
        per.nombre = input('Nombre: ')
        per.apellido = input('Apellido: ')
        per.edad = input('Edad: ')
        per.estatura = float(input('Estatura (en cm): '))
        per.peso = float(input('Peso (en kg): '))
        Personas.append(per)
        opc = input('¿Desea agregar otra persona? (y/n): ')
    print('-------IMC -----\n')
    for i in Personas:
        imc = i.calculo()
        rlt_imc = i.tbl_imc(imc)
        print(f'La persona: {i.nombre} {i.apellido},\n '
              f'peso: {i.peso} kg,\n '
              f'altura: {i.estatura} cm,\n '
              f'tiene un IMC: {round(imc, 1)},\n '
              f'y se encuentra en: {rlt_imc}\n')

if __name__ == "__main__":
    main()