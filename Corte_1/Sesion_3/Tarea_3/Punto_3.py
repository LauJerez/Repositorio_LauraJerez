# 3. Realizar un programa en el que se soliciten tres longitudes y con estos valores se determine si se puede hacer o no un triangulo. En el caso que se forme un triangulo, indicar si este es equilátero, isósceles o escaleno.

print('Ingrese tres longitudes para determinar si se puede hacer o no un triangulo: ')
l1=eval(input('Ingrese la longitud 1: '))
l2=eval(input('Ingrese la longitud 2: '))
l3=eval(input('Ingrese la longitud 3: '))

sum=l1+l2
if(sum>=l3):
  print('Si se puede formar un triangulo con las longitudes ingresadas')

  if(l1==l2) and (l1==l3):
    print('El tiangulo es equilatero')
  elif(l1==l2) or (l2==l3):
    print('El tiangulo es isosceles')
  else:
    print('El tiangulo es escaleno')

else:
  print('Las longitudes ingresadas no son validas para formar un triangulo')