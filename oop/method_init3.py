"""
Desarrollar una clase que presente un cuadrado y tenga los siguientes métodos.
Inicializar el valor del lado llegando como parámetro al método init(definir un atributo llamado lado),
imprimir su perímetro y su superficie.
"""
from modulefinder import LOAD_CONST


class Cuadrado:
    def __init__(self, lado):
        self.lado=lado 

    def mostrar_perimetro(self):
        perimetro=self.lado*4
        print("El perímetro del cuadrado es: ", perimetro)

    def mostrar_superficie(self):
        superficie=self.lado*self.lado
        print("La superficie del cuadrado es : ", superficie)

cuadrado1=Cuadrado(10)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()