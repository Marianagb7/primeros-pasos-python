"""
Desarrollar una palicación que nos permite crear un diccionario ingles/español.
La clave es la palabra en ingles y el valor es la clave en castellano.
Crear las siguientes funciones:
1. Cargar un diccionario.
2. Listado completo del diccionario.
3. Ingresar por teclado una palabra en ingles  y si existe en el diccionario mostrar su dirección.
"""
def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        ingles=input("Ingrese la palabra en ingles: ")
        castellano=input("Ingrese la palabra en castellano: ")
        diccionario[ingles]=castellano
        continua=input("¿Quiere ingresar otra palabra s/n ?: ")
    return diccionario
def imprimir(diccionario):
    print("Listado completo del diccionario: ")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en ingles a consultar: ")
    if pal in diccionario:
        print("En castellano significa", diccionario[pal])
    else:
        print("No se encuentra la traducción de la palabra")

#Bloque principal
diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)
        