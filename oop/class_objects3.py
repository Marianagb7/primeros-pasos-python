"""
Crear una clase que permita cargar el nombre y la edadde una persona.Mostrarlos datos cargados.
Imprimir si es mayor de edad(edad>=18)
"""
class Persona:

    def inicializar(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print("Nombre", self.nombre)
        print("Edad", self.edad)
    
    def mayor_edad(self):
        if self.edad>=18:
            print("Es mayor de edad: ")
        else:
            print("Es menor de edad")

#Bloque principal
persona1=Persona()
persona1.inicializar("Martha", 12)
persona1.imprimir()
persona1.mayor_edad()

persona2=Persona()
persona2.inicializar("Maria", 18)
persona2.imprimir()
persona2.mayor_edad()

persona3=Persona()
persona3.inicializar("Margot", 22)
persona3.imprimir()
persona3.mayor_edad()

