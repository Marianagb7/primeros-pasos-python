"""
Crear una función que cargue por teclado una lista de 5 enteros y la retorne. una segunda función debe 
recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa
llamar ambas funciones.
"""
def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor: "))
        li.append(valor)
    return li

def imprimir_mayores10(li):
    print("Elementos de la lista mayores a 10: ")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])
#Bloque principal
lista=carga_lista()
print(lista)
imprimir_mayores10(lista)