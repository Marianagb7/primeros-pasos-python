"""
Crear un diccionario en python que defina como clave el número de un documento de una persona y
como valor un string con su nombre.
Desarrollar las siguientes funciones:
1. Cargar los datos de cuatro personas.
2. Listado completo del diccionario.
3. consultando el nombre de la persona ingresando su número de documento.
"""
def cargar():
    personas={}
    for x in range(4):
        numero=int(input("Ingrese el número del documento: "))
        nombre=input("Ingrese nombre de la persona: ")
        personas[numero]=nombre
    return personas

def imprimir(personas):
    print("Listado completo del diccionario")
    for numero in personas:
        print(numero, personas[numero])

def consulta_por_numero(personas):
    nro=int(input("Ingrese número de documento para realizar la consulta: "))
    if nro in personas:
        print("Nombre de la persona: ", personas[nro])
    else:
        print("No existe persona con esa identificación")
#Bloque principal
personas=cargar()
imprimir=(personas)
consulta_por_numero(personas)
