"""
Definir una clase llamada punto con dos atributos x e y.
Crear método especial str para retornar un string con el formato (x, y)
"""
class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return "{"+str(self.x)+","+str(self.y)+"}"
punto1=Punto(10, 3)
punto2=Punto(-3, 12)
print(punto1)
print(punto2)
print(str(punto1)+ "       "+str(punto2))