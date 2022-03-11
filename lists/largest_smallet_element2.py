"""
Crear y cargar una lista con 5 enteros por teclado.
Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.
"""
list = []
for x in range(5):
    value = int(input("Ingrese valor: "))
    list.append(value)
smallet=list[0]
position=0
for x in range(1,5):
    if list[x]<smallet:
        smallet=list[x]
        position=x
print("Lista completa",list)
print("Menor de la lista", smallet)
print("Posición donde se encuentra el menor de la lista", position)