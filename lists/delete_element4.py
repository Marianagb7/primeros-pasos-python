"""
Crear una lista de 5 enteros y cargarlos por teclado.
Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.
"""

list1=[]
for x in range(5):
    value=int(input("Ingresa valor: "))
    list1.append(value)
print("Lista original")
print(list1)
list2=[]
position=0
while position < len(list1):
    if list1[position]>=10:
        list2.append(list1.pop(position))
    else:
        position=position+1
print("La lista original luego de borrar los elementos mayores o iguales a 10: ", list1)
print("Lista generada con los valores mayores o iguales a 10: ", list2)
