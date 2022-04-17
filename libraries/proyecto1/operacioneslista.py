def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista

def imprimir_mayor(lista):
    mayor=lista[0]
    for x in range(1, 5):
        if lista[x]>mayor:
            mayor=lista[x]
    print("Mayor elemento de la lista", mayor)

def imprimir_suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("La suma de sus elementos es: ", suma)