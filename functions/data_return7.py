"""
Crear una función que reciba un string en mayúscula o minúscula y retorne
 la cantidad de letras "a" o "A".
"""
def cantidad_vocales_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]== "a" or palabra[x]== "A":
           cant= cant+1
    return cant
#Bloque principal
palabra=input("Ingrese una palabra: ")
print("La palabra", palabra, "tiene", cantidad_vocales_a(palabra), "a")

