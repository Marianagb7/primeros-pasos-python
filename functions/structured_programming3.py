"""
Desarrollar un programa con dos funciones. La primera que  solicite el ingreso de un entero 
y muestre el cuadrado de dicho valor.
La segunda que solicite la carga de dos valores y muestre el producto de los mismos .
Llamar desde el bloque del programa principal ambas funciones.
"""
def calcular_cuadrado():
    valor=int(input("Ingrese un número entero: "))
    cuadrado=valor * valor
    print("El cuadrado del número es: ", cuadrado)
def calcular_producto():
    valor1= int(input("Ingrese el primer valor: "))
    valor2= int(input("Ingrese segundo valor: "))
    producto= valor1 * valor2
    print("El producto de los valores es: ", producto)
#Bloque principal
calcular_cuadrado()
calcular_producto()