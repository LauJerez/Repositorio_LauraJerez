class Estudiante:
    def __init__(self):                 
        self.__nombre = None              
        self.__apellido = None            
        self.__edad = None                
        self.__nacionalidad = 'Colombia'  

    def setNombre(self,nombre=str):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setApellido(self,apellido=str):
        self.__apellido=apellido

    def getApellido(self):
        return self.__apellido
    
    def setEdad(self,edad=str):
        if int(edad) > 21:
            self.__edad=edad
        else:
            self.__edad='Menor de edad'

    def getEdad(self):
        return self.__edad

    def entender(self):
        return 'Si, aprendi mucho hoy :)'
    
    def __licor(self):
        edad=self.__edad
        if int(edad)>21:
            return 'Puede beber Pola!'
        elif edad == 'Menor de edad':
            return 'Le toco jugo'
        
    def getLicor(self):
        return self.__licor()

def main():
    estudiante = []
    opc='n'
    while 1:
        est=Estudiante()
        # est.nombre=input('Nombre: ')
        # est.apellido=input('Apellido: ')
        # est.edad=input('Edad: ')
        est.setNombre(input('Nombre: '))
        est.setApellido(input('Apellido: '))
        est.setEdad(input('Edad: '))
        estudiante.append(est)
        opc=input('Desea Salir? (y/n)')
        if opc=='y':
            break
        else:
            print('Invalido')
    
    print(f'------------Clase 2023-II------------\n')
    for i in estudiante:
        print(f'Nombre: {i.getNombre()} {i.getApellido()}\n\
              Edad: {i.getEdad()}\n\n')
        print(est.getLicor())
        

if __name__=="__main__":
    main()