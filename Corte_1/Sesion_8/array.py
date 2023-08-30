
def main(cadena):
    for i in range(len(cadena)):
        print(cadena[i])
    
def main2(cadena):
    for i in cadena:
        print(i)

def main3(cadena):
    i=0
    while i<len(cadena):
        print(cadena[i])
        i+=1

def main4(cadena):
    for i in range(-1,-len(cadena)-1,-1):
        print(cadena[i])

if __name__=="__main__":
    cadena=[1,2,True,4.3,5,6,'Hola']
    #cadena='HOLA MUNDO'
    # main(cadena)
    # main2(cadena)
    # main3(cadena)
    main4(cadena)