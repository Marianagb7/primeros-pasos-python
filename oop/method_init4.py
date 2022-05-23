"""
Implementar la clase operaciones. Se deben cargar dos valores enteros por teclado en el metódo init,
calcular su suma, reta, multiplicación y división cada una en un método. Imprimir los resultados
"""
class Operaciones:
    def __init__(self):
        self.valor1=int(input("Ingrese el primer valor: "))
        self.valor2=int(input("Ingrese el segundo valor: "))
    
    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es: ", suma)
    
    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es: ", resta)

    def multiplicar(self):
        multiplicar=self.valor1*self.valor2
        print("El producto es", multiplicar)

    def dividir(self):
        dividir=self.valor1/self.valor2
        print("La división es: ", dividir)

operacion1=Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.dividir()