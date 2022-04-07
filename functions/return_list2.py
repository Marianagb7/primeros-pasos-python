"""
Construir una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función
debe recibir una lista y retornar el mayor y menor valor de la lista. Desde el bloque principal del 
programa llamar ambas funciones e imprimir el mayor y el menor de la lista.
"""
def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingresa valor: "))
        li.append(valor)
    return li

def retornar_mayormenor(li):
    may=li[0]
    men=li[0]
    for x in range(1,len(li)):
        if li[x]>may:
            may=li[x]
        else:
            if li[x]<men:
                men=li[x]
    return [men, may]

#Bloque principal
lista=carga_lista()
rango=retornar_mayormenor(lista)
print("El menor elemento de la lista: ", rango[0])
print("El mayor elemento de la lista: ", rango[1])

