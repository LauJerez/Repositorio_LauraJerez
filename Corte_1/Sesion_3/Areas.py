print('Seleccione una figura:\n'\
          '1.Circulo\n2.Triangulo\n3.Rectangulo')
fig=input('Seleccione una figura: ')
A='NO puede ser calculado'; figura=fig

if (fig.lower()=='circulo') or (fig=='1'):
    r=eval(input('Ingrese el radio: '))
    A=(3.1416*(r**2))
    figura='circulo'
elif (fig.lower()=='triangulo') or (fig=='2'):
    b=eval(input('Ingrese la base: '))
    h=eval(input('Ingrese la altura: '))
    A=(b*h)/2
    figura='triangulo'
elif (fig.lower()=='rectangulo') or (fig=='3'):
    b=eval(input('Ingrese la base: '))
    h=eval(input('Ingrese la altura: '))
    A=b*h  
    figura='rectangulo' 
else:
    print('Seleccione una figura valida')
print('Para un',figura,'el valor del area',A)