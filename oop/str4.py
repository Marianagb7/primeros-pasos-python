"""
Desarrolle un programa que implemente una clase llamada jugador.
Definir como atributos su nombre y su puntaje.
Codificar el método str que retorne el nombre y si es principiante(menos de 1000 puntos) o
experto(1000 o más puntos)
"""
class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def __str__(self):
        cadena=self.nombre+"_"
        if self.puntaje<1000:
            cadena=cadena+"principiante"
        else:
            cadena=cadena+"experto"
        return cadena

jugador1=Jugador("Ana", 700)
jugador2=Jugador("Juan", 2000)
print(jugador1)
print(jugador2)