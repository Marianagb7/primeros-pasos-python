"""
Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como 
valor el precio.
Desarrolar las funciones de:
1. Imprimir en forma completa el diccionario.
2. Imprimir solo artículos con precio superior a 100
"""
def cargar():
    productos={}
    for x in range(5):
        nombre=input("Ingrese el nombre del producto: ")
        precio=int(input("Ingrese el precio del producto: "))
        productos[nombre]=precio
    return productos

def imprimir(productos):
    print("Listado de todos los productos: ")
    for nombre in productos:
        print(nombre, productos[nombre])

def imprimir_mayores100(productos):
    print("Listado de productos con precio mayor a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)

#Bloque principal
productos=cargar()
imprimir(productos)
imprimir_mayores100(productos)