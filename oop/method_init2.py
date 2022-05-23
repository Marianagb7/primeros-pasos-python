"""
Desarrollar una clase  que presente un punto en el plano y tenga los siguientes  métodos inicializar los 
valores de x e y que llegan como párametros, imprimir en un cuadrante se encuentra en dicho punto. (Con-
cepto matemático, primer cuadrante si x e y son positivas, si x<0 y>0 segundo cuadrante, etc.)
"""
class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def imprimir(self):
        print("Coordenada del punto")
        print("(", self.x, ",", self.y, ")",sep="")

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrante")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")
                    else:
                        print("Esta en un eje")

punto1=Punto(10, 3)
punto1.imprimir()
punto1.imprimir_cuadrante()

punto2=Punto(-3, -4)
punto2.imprimir()
punto2.imprimir_cuadrante()

punto3=Punto(10, -3)
punto3.imprimir()
punto3.imprimir_cuadrante()


