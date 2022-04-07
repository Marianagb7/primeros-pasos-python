"""
Construir una función que nos retorne el perímetro de un cuadrado pasando como parametros 
el valor de un lado.
"""
def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro
#Bloque principal
lado=int(input("Ingrese un lado de un cuadrado: "))
print("El perímetro del cuadrado es: ", retornar_perimetro(lado))

