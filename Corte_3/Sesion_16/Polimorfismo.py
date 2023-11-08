class Ciudadano():
    def __init__(self,nombre:str,idioma:str):
        self.__nombre=nombre
        self.__idioma=idioma
    
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setIdioma(self,idioma:str):
        self.__idioma=idioma
    def getNombre(self):
        return self.__nombre
    def getIdioma(self):
        return self.__idioma
    #----------Sobrecarga------------
    def saludo(self):
        return f'Salut ca va'

class Colombiano(Ciudadano):
    def __init__(self, nombre: str, idioma: str,cc:str):
        super().__init__(nombre, idioma)
        self.__cc=cc
    
    def setCC(self,cc:str):
        self.__cc=cc
    def getCC(self):
        return self.__cc
    #----------Sobrecarga------------
    def saludo(self):
        return f'Quibo y entonces!, mi documento es {self.getCC()}'

class Ingles(Ciudadano):
    def __init__(self, nombre: str, idioma: str,id:str):
        super().__init__(nombre, idioma)
        self.__id=id

    def setId(self,id:str):
        self.__id=id
    def getId(self):
        return self.__id
    #-----------Sobrecarga---------
    def saludo(self):
        return f'Good day, good morning lads! , mi documento es {self.getId()}'

class Chino(Ciudadano):
    def __init__(self, nombre: str, idioma: str, sfz:str):
        super().__init__(nombre, idioma)
        self.__sfz=sfz
    
    def setSfz(self,sfz:str):
        self.__sfz=sfz
    def getSfz(self):
        return self.__sfz
    #-------------Sobrecarga------------
    def saludo(self):
        return f'你好，你干嘛呀！, mi documento es {self.getSfz()}'

def darSaludo(objeto):
    return objeto.saludo()

def main():
    persona1=Colombiano('Radamel García','Español','1725382303')
    persona2=Ingles('David Beckham','Ingles','AS21028')
    persona3=Chino('成龙','Mandarín','AD3LE334')
    persona4=Ciudadano('Carla Bruni','Frances')
    personas=[persona1,persona2,persona3,persona4]

    for ciudadanos in personas:
        print(f'\nMi nombre es: {ciudadanos.getNombre()},'\
             f'yo hablo: {ciudadanos.getIdioma()}')
        print(darSaludo(ciudadanos))


if __name__=="__main__":
    main()