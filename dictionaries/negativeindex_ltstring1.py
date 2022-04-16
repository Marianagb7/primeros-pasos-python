"""
Crear una función que reciba una reciba una palbra y verifique si es capicúa (es decir que se lee igual de 
izquierda a derecha que dederecha a izquierda)
"""
def capicua(cadena):
    iguales=0
    indice=-1
    for x in range(0, len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicúa")
    else:
        print("No es capicúa")

#Bloque principal
capicua("sometemos")
capicua("teléfono")