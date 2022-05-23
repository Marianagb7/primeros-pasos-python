"""
Crear una clase que represente un empleado. Definir como atributos su nombre y salario.
En el método init cargar los atributos por teclado y luego en otro método imprimir  sus datos y por 
último una que imprima un mensaje si debe pagar impuestos.(Si el sueldo supera a 3000)
"""
class Empleado:
    def __init__(self):
        self.nombre=input("Ingrese nombre del empleado: ")
        self.sueldo=float(input("Ingrese el salario: "))

    def imprimir(self):
        print("Nombre", self.nombre)
        print("Sueldo", self.sueldo)

    def paga_impuesto(self):
        if self.sueldo > 300:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")




empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuesto()
