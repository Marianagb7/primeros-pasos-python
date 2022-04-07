"""
Definir por asignación una lista de enteros en el bloque.
Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos los elementos,
la segunda recibe recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.
"""
def sumarlist(lista):
    suma=0
    for x in range(len(lista)):
        suma = suma+lista[x]
    return suma

def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]> may:
           may = lista[x]
    return may

def menor(lista):
    men=lista[0]
    for x in range(1, len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men




#Bloque principal
listavalores=[10, 20, 30, 40, 50]
print("Lista completa", listavalores)
print("La suma de todos sus elementos es: ", sumarlist(listavalores))
print("El mayor elemento de la lista es: ", mayor(listavalores))
print("El menor elemento de la lista es: ", menor(listavalores))