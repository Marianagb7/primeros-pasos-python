"""
Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con 
valor igual o superior 7.
"""

list = [1, 8, 22, 3, 4]
x=0
while x<len(list):
    if list[x]>=7:
        print(list[x])
    x=x+1

    