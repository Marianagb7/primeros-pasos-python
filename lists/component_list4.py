"""
se tiene la siguiente lista:
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de 
la lista. Volver a imprimir la lista.
"""
list = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
print(list)
for x in range(len(list[0])):
    if list[0][x]>50:
        list[0][x]=0
print(list)