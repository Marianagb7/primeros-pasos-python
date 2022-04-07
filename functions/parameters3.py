"""
Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular 
y mostrar su perímetro o superficie.
"""
from modulefinder import LOAD_CONST


def mostrar_perimetro(lado):
    per=lado*4
    print("El perímetro es: ", per)
def mostrar_superficie(lado):
    sup= lado * lado  
    print("La superficie es: ",sup)
def cargar_lado():
    la=int(input("Ingrese el valor del lado del cuadrado: "))
    respuesta=input("Quiere calcular el perímetro o la superficie (Ingresar texto: perímetro/superficie): ")
    if respuesta=="perímetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)

#Bloque principal
cargar_lado() 