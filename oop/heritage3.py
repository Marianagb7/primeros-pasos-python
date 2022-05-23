class Cuenta:
    def __init__(self, titular, monto):
        self.titular=titular
        self.monto=monto

    def imprimir(self):
        print("Titular: ", self.titular)
        print("Monto: ", self.monto)

class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()

class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, interes):
        super().__init__(titular, monto)
        self.plazo=plazo
        self.interes=interes
    
    def imprimir(self):
        print("Cuenta de plazo fijo")
        super().imprimir()
        print("Plazo en días: ", self.plazo)
        print("Intereses: ", self.interes)
        self.ganancia()
    
    def ganancia(self):
        ganancia=self.monto * self.interes/100
        print("Monto de interés", ganancia)

cajaahorro1=CajaAhorro("Antonio", "85000")
cajaahorro1.imprimir()
plazofijo1=PlazoFijo("Ana", 1000, 30, 0.75)
plazofijo1.imprimir()