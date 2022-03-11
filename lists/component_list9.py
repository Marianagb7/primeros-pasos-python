"""
Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que creamos en la lista.
El segundo valor indica la cantidad de elementos que tendra cada una de las listas internas a la lista
principal. Mostrar la lista y la suma de todos sus elementos.
"""
from sunau import AUDIO_FILE_ENCODING_LINEAR_24


list=[]
elements=int(input("Cuántos elementos tendrá la lista: "))
sublist=int(input("Cuántos elementos tendrá las listas internas: "))
for k in range(elements):
    list.append([])
    for x in range(sublist):
        value=int(input("Ingrese valor: "))
        list[k].append(value)
print(list)
add=0
for k in range(len(list)):
    for x in range(len(list[k])):
        add =add + list[k][x]
print("La suma de todos sus elementos es: ", add)