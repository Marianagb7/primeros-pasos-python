"""
Crear un programa con las siguientes funciones:
1. Cargar una lista de 5 enteros.
2. Retornar el mayor y menor valor de la lista mediante una tupla.
3. Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""
def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingres valor: "))
        lista.append(valor)
    return lista

def retornar_mayor_menor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1, len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    return(men, may)

#Bloque principal
lista=cargar()
menor, mayor=retornar_mayor_menor(lista)
print("Menor valor de la lista", menor)
print("Mayor valor de la lista", mayor)