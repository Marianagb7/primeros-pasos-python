"""
Crear una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres 
que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar la función dos veces.
Imprimir en el bloque principal cuál de los dos tiene mas caracteres.
"""
def largo(cadena):
    return len(cadena)
#Bloque principal

nombre1=input("Ingrese primer nombre: ")
nombre2=input("Ingrese segundo nombre: ")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("Los nombres tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1, "Es más largo")
    else:
        print(nombre2, "Es más largo")
        
