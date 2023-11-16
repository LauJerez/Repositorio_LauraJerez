class ciudadano():
    def _init_(self):

        self.__Nombre=None
        self.__Apellido=None
        self.__Edad=None
        self.__Documento=None

 #-----------------Getters---------------#
    def get_Nombre(self):
        return self.__Nombre
    
    def get_Apellido(self):
        return self.__Apellido
    
    def get_Edad(self):
        return self.__Edad
    
    def get_Documento(self):
        return self.__Documento

 #-------------------Setters-------------#

    def set_Nombre(self, Nombre):
        self.__Nombre=Nombre

    def set_Apellido(self, Apellido):
        self.__Apellido=Apellido

    def set_Edad(self, Edad):
        self.__Edad=int(Edad)

    def set_Documento(self, Valor_Documento):
        if len(Valor_Documento) >= 8 and len(Valor_Documento) <= 12:
            self.__Documento = Valor_Documento
        else:
            self.__Documento=None
            print('-----------Documento no válido--------------')


    def Mayor_Edad(self):
        if self.__Edad >= 18:
            print('----------- Eres legal-----------\n')
        else:
            print('-----------Eres ilegal------------\n')

    
    def Sobrecarga(self):
        print(f'es un buen ciudadano')

#---------------Clase Hijo Policia---------------

class policia(ciudadano):
    def init(self):
        ciudadano()._init_()
        self.Nplaca=None
        self.rango=None

    def get_Nplaca(self):
        return self.Nplaca
    
    def set_Nplaca(self, placa):
        if len(placa) >= 3 and len(placa) <= 6:
            self.Nplaca = placa
        else:
            self.Nplaca=None
            print('-----------NO es un policia!!!--------------')

    def get_rango(self):
        return self.rango
    
    def set_rango(self, rango):
        self.rango=rango

    def Sobrecarga(self):
        print(f'{self.get_Nombre()}  {self.get_Apellido()} es un gran policia')

#---------------Clase Hijo Psicologia---------------

class psicologia(ciudadano):
    def _init_(self):
        ciudadano()._init_()
        self.licencia=None
        self.especialidad=None

    def get_licencia(self):
        return self.licencia
    
    def set_licencia(self, licencia):
        if len(licencia) >= 4 and len(licencia) <= 8:
            self.licencia = licencia
        else:
            self.licencia = None
            print('-----------El psicologo no tiene licencia--------------')

    def get_especialidad(self):
        return self.especialidad
    
    def set_especialidad(self, especialidad):
        self.especialidad=especialidad

#---------------Clase Hijo Profesor---------------

class profesor(ciudadano):
    def _init_(self):
        ciudadano()._init_()
        self.Nclase=None
        self.materia=None

    def get_Nclase(self):
        return self.Nclase
    
    def set_Nclase(self, Nclase):
        if len(Nclase) >= 0 and len(Nclase) <= 4:
            self.Nclase = Nclase
        else:
            self.Nclase = None
            print('-----------El numero de clase no existe--------------')

    def get_materia(self):
        return self.materia
    
    def set_materia(self, materia):
        self.materia=materia

def main():
    Persona=ciudadano()
    hijo1=policia()
    hijo2=psicologia()
    hijo3=profesor()


    while True:
        Persona.set_Nombre(input('Nombre: '))
        Persona.set_Apellido(input('Apellido: '))
        Persona.set_Edad(input('Edad: '))
        Persona.set_Documento(input('Documento: '))

        print('--------------------policia-----------------')
        hijo1.set_Nplaca(input('Ingrese se #placa: '))
        hijo1.set_rango(input('Rango: '))
        

        print('--------------------psicologia--------------------')
        hijo2.set_licencia(input('licencia: '))
        hijo2.set_especialidad(input('especialidad: '))
        
        print('----------------------profesor---------------------')
        hijo3.set_Nclase(input('Ingrese #clase: '))
        hijo3.set_materia(input('materia: '))

        print('\n\n\n\n\n__________________________________\n')
        print(f'Nombre: {Persona.get_Nombre()}')
        print(f'Apellido: {Persona.get_Apellido()}')
        print(f'Edad: {Persona.get_Edad()}')
        print(f'Documneto: {Persona.get_Documento()}')
        Persona.Mayor_Edad()
        print('--------------------policia-----------------')
        print(f'#placa: {hijo1.get_Nplaca()}')
        print(f'rango: {hijo1.get_rango()}')
    
        print('\n--------------------psicologia--------------------')
        print(f'licencia: {hijo2.get_licencia()}')
        print(f'especialidad: {hijo2.get_especialidad()}')
       
        print('\n----------------------profesor---------------------')
        print(f'#clase: {hijo3.get_Nclase()}')
        print(f'materia: {hijo3.get_materia()}\n\n\n\n\n')
        
        Persona.Sobrecarga()
        hijo1.Sobrecarga()

if _name=='main_':
    main()