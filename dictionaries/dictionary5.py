"""
Crear un programa  que permita cargar un código de un producto como clave de diccionario.
Guardar para dicha clave una tupla con el nombre  del producto su precio y cantidad en stock.
Implementar las siguientes actividades:
1. Cargar datos en el diccionario.
2. Listado completo de productos.
3. Consulta de un producto por su clave, mostrar el nombre, precio y stock.
Listado de todos los productos que tengan un stock con valor cero.
"""
def cargar():
    productos={}
    continua="s"
    while continua =="s":
        codigo=int(input("Ingresar el código del producto: "))
        descripcion=input("Ingrese la descripción del producto: ")
        precio=float(input("Ingrese precio: "))
        stock=int(input("Ingrese stock actual: "))
        productos[codigo]=(descripcion, precio, stock)
        continua=input("Desea cargar otro producto s/n: ")
    return productos

def imprimir(productos):
    print("Listado de productos: ")
    for codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

def consulta(productos):
    codigo=int(input("Ingrese el código  de articulo a consultar: "))
    if codigo in productos:
        print(productos[codigo][0],  productos[codigo][1], productos[codigo][2])

def listado_stock_cero(productos):
    print("Listado de articulos con stock cero")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo, productos[codigo][0], productos[codigo][1])
#Bloque principal
productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)
        