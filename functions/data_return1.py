"""
Construir una función que le enviamos como parámetro el valor lado de un cuadrado y nos retorne la
superficie.
"""
def retornar_superficie(lado):
    sup=lado*lado
    return sup
#Bloque principal
la=int(input("Ingrese el valor del lado del cuadrado: "))
superficie=retornar_superficie(la)
print("La superficie del cuadrado es: ", superficie)