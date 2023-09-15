class Estudiante:
    def __init__(self):                 #
        self.nombre = None              #
        self.apellido = None            #   constructor
        self.edad = None                #
        self.nacionalidad = 'Colombia'  #

    def entender(self):
        return 'Si, aprendi mucho hoy :)'

def main():

    est1 = Estudiante()      # Instancia y Puntuador
    est1.nombre = 'Juan'     #
    est1.apellido = 'Picon'  #  Objeto No.1
    est1.edad = 17           #


    est2 = Estudiante()        # Instancia y Apuntuador
    est2.nombre = 'Roger'      #
    est2.apellido = 'Piñeros'  #  Objeto No.2
    est2.edad = 17             #


    print(f'El estudiante: {est2.nombre} {est2.apellido}, '\
          f'tiene una edad de: {est2.edad}',\
            f'y su nacionalidad es: {est2.nacionalidad}')
    input('Entendió?')
    print( est2.entender())


if __name__=="__main__":
    main()