# 2. Realice un programa para cobrar el tiempo de parqueo en un estacionamiento, donde se cobra $139 el minuto. mostrar el valor total, discriminando el IVA, aproximando a la cifra de $50 siguiente.
tiempo=eval(input("Ingrese el tiempo de parqueo(En minutos): "))
valor=tiempo*139
IVA=valor*0.19
To=valor+IVA
val_total=round(To,-1)
if val_total%50!=0:
  val_total+=50-val_total%50
  print('Para',tiempo,'minutos, el valor del IVA es',round(IVA, 2), 'y el valor total es',val_total)