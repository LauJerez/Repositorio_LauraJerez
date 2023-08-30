n=int(input('Ingrese la cantidad de primos solicitada: '))
con=1;x=2
numero = '1 '

while con <n:
    for i in range (2,x+1):
        primo=x%i
        if primo==0 and x==i:
            numero += str(f' {x} ')
            con+=1 
        elif primo==0 and x!=i:
            break
    x+=1
print(numero)