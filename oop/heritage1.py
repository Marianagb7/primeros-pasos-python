"""
Plantear una clase persona que contenga dos atributos: nombre y edad. Definir como responsabilidades
la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar sus métodos.
Declarar una segunda clase llamada Empleado que herede de la clase persona y agregue un atributo sueldo y
muestre se debe pagar impuestos(sueldos superior a 3000)
También en el bloque principal del programa crear un objeto de la clase empleado.
"""
class Persona:
    def __init__(self):
         self.nombre=input("Ingrese el nombre: ")
         self.edad=int(input("Ingrese la edad: "))

    def imprimir(self):
        print("Nobre", self.nombre)
        print("Edad", self.edad)
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese salario: "))

    def imprimir(self):
        super().imprimir()
        print("Salario", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print(self.nombre, "Debe pagar impuestos")
        else: 
            print(self.nombre, "No paga impuestos")

#Bloque principal
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

