"""
Realizar un programa que pida la carga de dos listas númericas enteras de 4 elementos cada una.
Generar una tercera lista que surja de la suma de los elementos de la misma pocisión de cada lista.
Mostrar tercera lista.
"""
list1=[]
print("Ingresa primera lista")
for x in range(4):
    value=int(input("Ingrese valor: "))
    list1.append(value)
print("Ingresa segunda lista")
list2=[]
for x in range(4):
    value=int(input("Ingrese valor: "))
    list2.append(value)
list_add=[]
for x in range(4):
     add=list1[x]+list2[x]
     list_add.append(add)
print("Primera lista", list1)
print("Segunda lista", list2)
print("Tercera lista, suma de listas 1 y 2", list_add)

