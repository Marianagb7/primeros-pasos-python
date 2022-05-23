"""
Implementar una clase llamada alumno que tenga como atributos su nombre y su nota. Definir los métodos 
para inicializar sus atributos.Imprimirlos y mostrar un mensaje si está regular(nota menor o igual a 4)
Definir 2 objetos de la clase alumno
"""
class Estudiante:
    def inicializar(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre", self.nombre)
        print("Nota", self.nota)
    
    def mostrar_estado(self):
        if self.nota<=4:
            print(self.nombre, "Regular")
        else:
            print(self.nombre, "Estas muy bien")
#Bloque principal

estudiante1= Estudiante()
estudiante1.inicializar("Carlos", 8)
estudiante1.imprimir()
estudiante1.mostrar_estado()

estudiante2= Estudiante()
estudiante2.inicializar("Felipe", 3)
estudiante2.imprimir()
estudiante2.mostrar_estado()
