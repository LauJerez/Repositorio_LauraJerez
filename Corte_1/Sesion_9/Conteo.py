def conteo(num):
    
    if num>0:
        num-=1
        conteo(num)
    else:
        print(num)
    print(num+1)

if __name__=="__main__":
    n=int(input('Hasta que numero desea contar: '))
    conteo(n)