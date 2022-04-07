"""
Crear una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18.
Como mínimo se envía un número entero a la función.
"""
def cantidad_mayores18(edad, *edades):
    cant=0
    if edad>=18:
        cant= cant+1

    for x in range(len(edades)):
        if edades[x]>=16:
            cant=cant+1
    return cant

#Bloque principal
print("Cantidad de personas mayores a 18 años son:", cantidad_mayores18(25, 16, 3, 44, 36, 2, 19, 18, 22,13))
