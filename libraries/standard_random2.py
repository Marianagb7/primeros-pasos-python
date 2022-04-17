"""
Crear un programa que cargue una lista de 10 enteros.
Cargar valores aleatorios con números enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo.
"""
import random


def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,100))
    return lista

def imprimir(lista):
    print(lista)

def mezclar(lista):
    random.shuffle(lista)

#Bloque principal
lista=cargar()
imprimir(lista)
mezclar(lista)
imprimir(lista)