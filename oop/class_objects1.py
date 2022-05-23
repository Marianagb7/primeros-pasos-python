"""
Implementaresmos una clase llamada persona que tendrá como atributo su nombre y dos métodos, un método
inicializará el atributo nombre y el siguiente mostrara por pantalla el contenido del mismo.
Definir dos objetos de la clase persona.
"""
class Persona:
    def inicializar(self, nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre", self.nombre)

#Bloque principal
persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Antonio")
persona2.imprimir()