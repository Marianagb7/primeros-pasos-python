"""
En el bloque principal del programa definir un diccionario que almacene los nombres de países como clave y 
como valor la cantidad de habitantes.
Implementar una función para mostrar cada clave valor.
"""
def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

#Bloque principal
paises={"Brasil": 210867954, "China": 1415045928, "India": 1354051854, "México":130759014}
imprimir(paises)