"""
Crear y cargar una lista con 5 enteros, implementar un algoritmo que identifique el mayor valor de la
lista.
"""
list = []
for x in range(5):
    value=int(input("Ingrese valor: "))
    list.append(value)
largest=list[0]
for x in range(1,5):
    if list[x]>largest:
        largest=list[x]
print("Lista completa",list)
print("Mayor lista", largest)