# 3. Realice un programa que solicite una temperatura en escala Fº (decimal) y muestre el equivalente en grados Cº.
GF = int(input('Ingrese los grados Fahrenheit: '))
GC = (GF-32)*(5/9)
print('La cantidad de grados Fahrenheit',GF,'corresponden a',GC,'grados Celsius')