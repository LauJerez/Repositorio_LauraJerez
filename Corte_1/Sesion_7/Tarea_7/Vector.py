# Vector
import math as m

def vector():
  c1=eval(input('Ingrese la coordenada de origen del vector:'))
  c2=eval(input('Ingrese la coordenada de fin del vector:'))

  modulo= m.sqrt((c1**2)+(c2**2))
  print(f'el modulo del vector {c1,c2} es: {modulo}')

  com_r= m.degrees(m.atan(c2/c1))
  print(com_r)
  print(f'Sus componentes rectangulares son {modulo, com_r}')



if __name__=="__main__":
  vector()