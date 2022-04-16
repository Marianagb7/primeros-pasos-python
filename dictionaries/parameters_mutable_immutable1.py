"""
Confeccinar un programa que contenga las siguientes funciones:
1. Carga de una lista y retorno al bloque principal.
2. Fijar en cero todos los elementos de la lista que tenga  un valor menor a 10.
3. Imprimir la lista.
"""
def carga():
    lista=[]
    continua="s"
    while continua =="s":
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
        continua=input("Agrega otro elemento a la lista s/n: ")
    return lista

def fijar_cero(lista):
    for x in range(len(lista)):
        if lista[x]<10:
            lista[x]=0

#Bloque principal
lista=carga()
print(lista)
fijar_cero(lista)
print(lista)
