"""
Crear una clase club y otra clase socio.
La clase socio debe tener los siguientes tres atributos nombre y la antiguedad en el club(en años).
En el método init de la clase socio pedir la carga por teclado del nombre y su antiguedad.
La clase club debe tener como atributos 3 objetos de la clase socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antiguedad en el club.
"""
class Socio:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del socio: ")
        self.antiguedad=int(input("Ingrese los años de antiguedad: "))

    def imprimir(self):
        print(self.nombre, "tiene antiguedad de ", self.antiguedad, "años")
    
    def retornar_antiguedad(self):
        return self.antiguedad

class Club:
    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()

    def mayor_antiguedad(self):
        print("Socio con mayor antiguedad")
        if (self.socio1.retornar_antiguedad()>self.socio2.retornar_antiguedad()
             and self.socio1.retornar_antiguedad()>self.socio3.retornar_antiguedad()):
            self.socio1.imprimir()
        else:
            if self.socio1.retornar_antiguedad()>self.socio3.retornar_antiguedad():
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()
#Bloque principal
clud1=Club()
clud1.mayor_antiguedad()