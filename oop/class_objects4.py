"""
Desarrollar un programa que cargue los lados de un triangulo por teclado e implemente los siguientes 
métodos:
1. Inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equílatero
o no. El nombre de la clase llamarla triangulo.
"""
class Triangulo:
    def inicializar(self):
        self.lado1=int(input("Ingrese primer lado: "))
        self.lado2=int(input("Ingrese el segundo lado: "))
        self.lado3=int(input("Ingrese tercer lado: "))

    def imprimir(self):
        print("Lado 1", self.lado1)
        print("Lado 2", self.lado2)
        print("Lado 3", self.lado3)

    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)
    
    def es_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")
#Bloque principal
triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()
