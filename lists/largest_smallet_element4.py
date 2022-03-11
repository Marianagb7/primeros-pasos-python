"""
Cargar una lista con 5 elementos enteros.Imprimnir el mayor y un mensaje si se repite
dentro de la lista.(Es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""
list = []
for x in range(5):
    value=int(input("Ingresa valor: "))
    list.append(value)
major=list[0]
for x in range(1, 5):
    if list[x]>major:
        major = list[x]
print("Lista completa", list)
print("Mayor de la lista", major)
quantity=0
for x in range(5):
    if list[x]==major:
        quantity=quantity+1
if quantity >1:
    print("El valor mayor se encuentra repetido en la lista", )