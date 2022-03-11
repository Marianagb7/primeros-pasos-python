"""
Cargar una lista con 5 elementos enteros ordenarla de menor a mayor. Mostrarla por pantalla, luego
ordenarla de mayor a menor e imprimirla nuevamente.
"""
list=[]
for x in range(5):
    value=int(input("Ingrese valor:"))
    list.append(value)
# Ordenamiento de menor a mayor
for k in range (4):
    for x in range(4-k):
        if list [x]>list[x+1]:
            aux=list[x]
            list[x]=list[x+1]
            list[x+1]=aux
print("Lista ordenada de menor a mayor", list)
# Ordenamiento de mayor a menor

for k in range(4):
    for x in range(4-k):
        if list[x]<list[x+1]:
            aux=list[x]
            list[x]=list[x+1]
            list[x+1]=aux
print("Lista de mayor a menor", list)