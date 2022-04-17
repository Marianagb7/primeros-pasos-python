"""
Desarrollar un programa que solicite la carga de un valor entero por teclado y luego nos muestre
la raíz cuadrada del número y el valor elevado al cubo.
"""
from math import sqrt, pow

valor=int(input("Ingrese  un número entero: "))
valor1=sqrt(valor)
valor2=pow(valor, 3)
print("La raíz cuadrada", valor1)
print("El cubo", valor2)