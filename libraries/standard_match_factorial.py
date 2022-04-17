#Calcular el factorial de un número ingresado por teclado. 
from math import factorial

valor=int(input("Ingrese un valor: "))
resultado=factorial(valor)
print("El factorial de: ", valor, "es", resultado)