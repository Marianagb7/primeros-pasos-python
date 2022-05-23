"""
Definir una clase Rectangulo.
Definir dos atributos(ladomenor, y lado mayor). Redefinir el operador == de tal forma 
que tenga en cuenta la superficie del rectángulo.
"""
from inspect import classify_class_attrs


class Rectangulo:
    def __init__(self, ladomenor, ladomayor):
        self.ladomenor=ladomenor
        self.ladomayor=ladomayor

    def retornar_superficie(self):
        return self.ladomenor*self.ladomayor

    def __eq__(self, objeto2):
        if self.retornar_superficie()==objeto2.retornar_superficie():
            return True
        else:
            return False

rectangulo1=Rectangulo(10, 10)
rectangulo2=Rectangulo(5, 20)
if rectangulo1==rectangulo2:
    print("Los rectangulos tienen la misma superficie")