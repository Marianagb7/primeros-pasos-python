"""
Definir una lista y luego solicitar la carga de 5  enteros por teclado y añadirlos a la lista.
Imprimir la lista generada.
"""
from multiprocessing.sharedctypes import Value


numbers=[]
for x in range(5):
    value=int(input("Ingresa un valor entero: "))
    numbers.append(value)
print(numbers)
print(len(numbers))

