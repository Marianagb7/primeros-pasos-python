"""
Crear una lista de enteros por asignación, definir una función que reciba una lista de enteros y un
segundo parámetro de tipo entero. Dentro de la función mostrar cada elemnto de la lista multiplicando 
por el valor entero enviado.
"""
def multiplicar(lista, valor):
    for x in range(len(lista)):
        multi=lista[x]*valor
        print(multi)

#Bloque principal 
lista=[3, 7, 8, 10, 2]
print("Lista original", lista)
print("Lista de los elementos múltiplicados por 3: ")
multiplicar(lista, 3)
