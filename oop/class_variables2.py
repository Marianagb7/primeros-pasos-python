"""
Crear una clase llamada Jugador
Definir en la clase jugador los atributos nombre, puntaje y los metodos init, imprimir, pasar_tiempo(que debe
reducir en uno la variable de clase que indique cuantos minutos faltan para el fin del juego"iniciara con el valor 30)
Definir en el bloque principal dos objetos de la clase jugador.
Reducir la variable de la clase de uno en uno hasta llegar a cero.
"""
class Jugador:
    tiempo=30
    def __init__(self, nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def imprimir(self):
        print("Nombre", self.nombre)
        print("Puntaje", self.puntaje)
        print("Fin del juego en: ", Jugador.tiempo, "minuto")

    def pasar_minuto(self):
        Jugador.tiempo=Jugador.tiempo-1

#Bloque principal
jugador1=Jugador("Ana", 100)
jugador2=Jugador("Juan", 50)

while Jugador.tiempo >0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_minuto()
