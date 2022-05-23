class Persona:
    def __init__(self, nom, ape):
        self.nombre=nom
        self.apellido=ape
    def __str__(self):
        cadena=self.nombre+","+self.apellido
        return cadena
persona1=Persona("José", "Mora")
persona2=Persona("Ana", "Peña")
print(str(persona1)+"-"+str(persona2))
