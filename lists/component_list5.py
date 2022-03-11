"""
Con la lista dada.
Imprimir la lista.
Luego fijar con el valor 0 todos los elementos mayores a 10, contenidos en todos los elementos 
de la variable lista.
Volver a imprimir la lista.
"""
list=[[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78,56]]
print(list)
for k in range(len(list)):
    for x in range(len(list[k])):
        if list[k][x]>10:
            list[k][x]=0
print(list)
