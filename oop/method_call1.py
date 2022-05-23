"""
Definir una clase operaciones que solicite un método init para la carga de dos enteros e inmediatamente
muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de la clase 
operación y llamarlos desde el mismo método init.
"""
class Operaciones:
    def __init__(self):
        self.valor1=int(input("Ingrese primer valor: "))
        self.valor2=int(input("Ingrese segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
    
    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es: ", suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta", resta)

    def multiplicar(self):
        multi=self.valor1*self.valor2
        print("El producto es: ",multi)

    def dividir(self):
        divi=self.valor1/self.valor2
        print("La división es: ", divi)


operaciones1=Operaciones()