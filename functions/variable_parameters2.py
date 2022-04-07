"""
Confeccionar una función que reciba 3 enteros y retorne la suma. Llamar a la función enviando 3 enteros
que se encuentran almacenados en una lista.
"""
def sumar(v1, v2, v3):
    return v1+v2+v3
#Bloque principal
lista=[1, 2, 3]
print(sumar(lista[0], lista[1], lista[2]))
print(sumar(*lista))
