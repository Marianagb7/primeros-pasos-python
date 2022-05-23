"""
Crear una clase cliente de un banco y redefiniremos el operador + para que nos retorne la suma de los
depósitos de los depositos de los clientes que estamos sumando.
"""
class Cliente:
    def __init__(self, nombre, monto):
        self.nombre=nombre
        self.monto=monto

    def __add__(self, objeto2):
        suma=self.monto+objeto2.monto
        return suma
cliente1=Cliente("Ana", 1500)
cliente2=Cliente("Carlos", 1000)
print("Total depositado por los clientes")
print(cliente1+cliente2)