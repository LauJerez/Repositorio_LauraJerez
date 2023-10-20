class Deportista():
    def __init__(self,nombre:str,edad:int,documento:str):
        self.__nombre=nombre
        self.__edad=edad
        self.__documento=documento
    
    #-------------Setters-------------

    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setEdad(self,edad:int):
        self.__edad=edad

    def setDocumento(self,documento:str):
        self.__documento=documento

    #-------------Getters-------------
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getDocumento(self):
        return self.__documento
    
    def jugador(self):
        return f'El jugador {self.getNombre()} es un gran maestro ajedrecista'
        
class Futbolista(Deportista):
    def __init__(self,nombre:str,edad:int,documento:str,nombre_equipo:str,goles:int):
        super().__init__(nombre, edad, documento)
        self.nombre_equipo=nombre_equipo
        self.goles=goles
    
    #-------------Setters-------------
    def setNombreEquipo(self,nombre_equipo:str):
        self.nombre_equipo=nombre_equipo

    def setGoles(self,goles:int):
        self.goles=goles

    #-------------Getters-------------
    def getNombreEquipo(self):
        return self.nombre_equipo
    
    def getGoles(self):
        return self.goles
    
    #-------------Métodos-------------
    def patear(self):
        return f'El jugador {self.getNombre()} acaba de anotar un gol'
    
    def jugador(self):
        return f'El jugador {self.getNombre()} es un gran delantero'
    
class Tenista(Deportista):
    def __init__(self,nombre:str,edad:int,documento:str,set_ganados:int,ace:int):
        super().__init__(nombre, edad, documento)
        self.set_ganados=set_ganados
        self.ace=ace

    #-------------Setters-------------
    def setSet_ganados(self,set_ganados:str):
        self.set_ganados=set_ganados

    def setAce(self,ace:int):
        self.ace=ace

    #-------------Getters-------------
    def getSet_ganados(self):
        return self.set_ganados
    
    def getGoles(self):
        return self.ace
    
    #-------------Métodos-------------
    def Ace(self):
        return f'El jugador {self.getNombre()} acaba de hacer un punto'
    
    def jugador(self):
        return f'El jugador {self.getNombre()} es un gran tenista'

def main():
    jugador_1=Futbolista('Radamel Falcao García',35,'123456789','Colombia',34)
    jugador_2=Tenista('Roger Federer',42,'987654321',6,12)
    jugador_3=Deportista('Magnus Carlsen',32,'963852741')
    
    print(jugador_2.jugador())
    print(jugador_2.Ace())
    print('-------------------')
    print(jugador_1.jugador())
    print(jugador_1.patear())
    print('-------------------')
    print(jugador_3.jugador())

if __name__=="__main__":
    main()