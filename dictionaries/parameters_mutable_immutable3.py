"""
Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y 
como valor su número teléfonico.
1. Cargar de contactos.
2. Permitir modificar el número teléfonico. Se ingresa el nombre de contacto para su búsqueda.
3. Imprimir la lista completa de contactos con sus número teléfonicos.
"""
def cargar():
    contactos={}
    continua="s"
    while continua=="s":
        nombre=input("Ingrese el nombre del contacto: ")
        telefono=input("Ingrese el número de teléfono: ")
        contactos[nombre]=telefono
        continua=input("Desea agregar otro contacto s/n: ")
    return contactos

def modificar_telefono(contactos):
    nombre=input("Ingrese el nombre del contacto o modificar su teléfono: ")
    if nombre in contactos:
        telefono=input("Ingrese el nuevo número: ")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado: ")

def imprimir(contactos):
    print("Listado de todos los contactos")
    for nombre in contactos:
        print(nombre, contactos[nombre])
        
#Bloque principal
contactos=cargar()
modificar_telefono(contactos)
imprimir(contactos)