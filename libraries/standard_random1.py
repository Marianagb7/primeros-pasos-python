"""
Construir un programa que simule tirar dados y luego muestre los valores que salieron.
Imprimir un mensaje que gano si la suma de los dados es igual a 7.
"""
import random

dado1=random.randint(1,6)
dado2=random.randint(1, 6)
print("Primer dado: ",dado1)
print("Segundo dado: ",dado2)
suma=dado1+dado2
if suma == 7:
    print("Gano")
else:
    print("Perdio")
