"""
Crear una función que reciba entre 2 y n(siendo n=2, 3, 4, 5, 6 etc) valores enteros, retornar la suma
de dichos parámetros.
"""
def sumar(v1, v2, *lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
#Bloque principal
print(sumar(1,2))
print(sumar(1,2,3,4,5))
print(sumar(1, 2, 3))
