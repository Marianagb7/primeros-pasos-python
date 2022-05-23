"""
Crear una clase Persona que tenga los atributos de nombre y edad.
El operador == retornará verdadero si las personas tienen la misma edad, el operador > retornará True 
si la edad del objeto de la izquierd tiene una edad mayor a la edad objeto de la derecha del operador >,
y así sucesivamente.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def __eq__(self, object2):
        if self.edad==object2.edad:
            return True
        else:
            return False

persona1=Persona("Juan", 22)
persona2=Persona("Ana", 10)
if persona1==persona2:
    print("Tienen la misma edad")
else:
    print("No tienen la misma edad")