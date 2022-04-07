"""
Definir una lista de enteros por asignación en el bloque principal. Llamar una función que reciba la 
lista  y nos retorne el producto de todos sus elementos . Mostrar dicho produto en el bloque
 principal de nuestro programa
"""
def producto(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod
lista=[12,10,5]
print(lista)
print("La multiplicación de los elementos de la lista es: ", producto(lista))
