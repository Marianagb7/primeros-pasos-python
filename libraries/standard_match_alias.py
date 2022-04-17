"""
Confeccionar un programa que solicite la carga por teclado y luego nos muestre la raíz cuadrada
del número y el valor al cubo.
"""
from math import sqrt as raiz_cuadrada, pow as cubo

valor=int(input("Ingrese un valor entero: "))
print("La raiz cuadrada es", raiz_cuadrada(valor))
print("El cubo", cubo(valor, 3))