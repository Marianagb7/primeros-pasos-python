"""
Realizar un programa que contenga las siguientes funciones:
1. Crgar una lista de 10 enteros.
2. Recibir una lista y retornar otra con la primera mitad.(se sabe que siempre llega una lista con una
cantidad par de elementos)
3. Imprimir una lista.
"""
def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista

def retornar_mitad(lista):
    mitad=len(lista)//2
    return lista[:mitad]

def imprimir(lista):
    print("Contenido de la lista")
    print(lista)

#Bloque principal
lista=cargar()
lista2=retornar_mitad(lista)
imprimir(lista)
imprimir(lista2)

