"""
Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma
en la misma línea.
"""
def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor: "))
        lista.append(valor)
    return lista

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end="-")

#Bloque principal
lista=cargar()
imprimir(lista)
