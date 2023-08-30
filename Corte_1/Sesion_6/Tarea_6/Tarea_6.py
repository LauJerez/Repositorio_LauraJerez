print('Seleccione el programa a realizar: \n'\
                  '1. Divisores positivos\n'\
                  '2. Producto entre dos números enteros\n'\
                  '3. Serie de Fibbonacci\n')
sel=input('Selececione el programa: ')

if (sel.lower() =='Divisores positivos') or (sel=='1'):

   n= int(input('Ingrese un número: '))
   if n == 0:
    print('Ningún número es divisible entre cero')
   else:
    print('Los divisores positivos de', n, 'son:')
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

elif (sel.lower()=='Producto entre dos números enteros') or (sel=='2'):

   num1 = int(input('Ingrese un numero: '))
   num2 = int(input('Ingrese el segundo numero: '))

   producto = 0
   for i in range(abs(num2)):
    producto += abs(num1)

   if num1 < 0 and num2 < 0:
    producto = abs(producto)
   elif num1 < 0 or num2 < 0:
    producto = -producto
   print('Producto:',producto)

elif (sel.lower()=='Serie de Fibbonacci') or (sel=='3'):

    N = int(input('Ingrese el numero de digitos de la serie de fibonacci que desea saber: '))
    num1= 0
    num2= 1
    if N <= 0:
     print('La serie de Fibonacci es vacía.')
    elif N == 1:
     print('La serie de Fibonacci es: ',num2)
    else:
     print('La serie Fibonnci es:  ')
    for i in range(N):
     print(num1, end= ' ' )
     num3= num1 + num2
     num1=num2
     num2=num3
else:
  print('Programa seleccionado invalido')