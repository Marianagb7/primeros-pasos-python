"""
Confeccionar un programa que permita.
1. Cargar una lista de 10 elementos enteros.
2. Generar dos listas a partir de la rpimera. En una guardar los valores positivos y en otra los negativos
Imprimir las dos listas generadas.
"""
def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista

def generar_listas(lista):
    listanegativa=[]
    listapositiva=[]
    for x in range(len(lista)):
        if lista[x]<0:
            listanegativa.append(lista[x])
        else:
            if lista[x]>0:
                listapositiva.append(lista[x])
    return(listanegativa, listapositiva)

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])

#Bloque principal
lista=cargar()
listanegativa, listapositiva=generar_listas(lista)
print("Lista con valores negativos")
imprimir(listanegativa)
print("Lista valores positivos")
imprimir(listapositiva)




        