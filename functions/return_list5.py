"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1. Cargar los nombres de los artículos y sus precios.
2. Imprimir los nombres y precios
3. Imprimir el nombre de artículos con un precio mayor.
4. Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor o igual al valor 
ingresado.
"""
def cargar_datos():
    articulos=[]
    precios=[]
    for x in range(5):
        ar=input("Ingrese nombre del artículo: ")
        articulos.append(ar)
        pre=int(input("Ingrese el precio de dicho artículo: "))
        precios.append(pre)
    return(articulos, precios)

def imprimir(articulos, precios):
    print("Listado completo de artículos y precios: ")
    for x in range(len(articulos)):
        print(articulos[x], precios[x])

def precio_mayor(articulos, precios):
    may=precios[0]
    pos=0
    for x in range(1, len(precios)):
        if precios[x]>may:
            may=precios[x]
            pos=x
    print("Articulos con un precio mayor: ", articulos[pos], "su precio es", may)

def consulta_precio(articulos, precios):
    valor=int(input("Ingrese un importe para mostrar los artículos con un precio menor: "))
    for x in range(len(precios)):
        if precios[x]<=valor:
            print(articulos[x], precios[x])
            
#Bloque principal
articulos, precios=cargar_datos()
imprimir(articulos, precios)
precio_mayor(articulos, precios)
consulta_precio(articulos, precios)