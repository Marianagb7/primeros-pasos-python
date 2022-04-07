"""
Construir una función que calcule la superficie de un rectángulo y la retorne. La función recibe como parámetro 
los valores de dos de sus lados.
En el bloque principal del programa cargardos rectangulos y luego mostrar cuál de los dos tiene mayor
superficie. 
"""
def retorna_superficie(lado1, lado2):
    superficie= lado1*lado2
    return superficie
#Bloque principal
print("Primer retángulo")
lado1=int(input("Ingrese el lado menor del retángulo: "))
lado2=int(input("Ingrese el lado mayor del rectángulo: "))
print("Segundo rectangulo")
lado3=int(input("Ingrese el lado menor del rectángulo: "))
lado4=int(input("Ingresa el lado mayor del rectángulo: "))
if retorna_superficie(lado1, lado2)==retorna_superficie(lado3, lado4):
    print("Los rectángulos tienen la misma superficie")
else:
    if retorna_superficie(lado1, lado2)>retorna_superficie(lado3, lado4):
        print("El primer rectángulo tiene una mayor superficie: ")
    else:
        print("El segundo rectangulo tiene una superficie mayor: ")
