"""
Declarar una clase llamada familia. Definir como atributos el nombre del padre, madre y una
lista con los nombres de los hijos.
Definir el método especial str que retorne un string con el nombre del padre, madre y de todos sus hijos.
"""
class Familia:
    def __init__(self, padre, madre, hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__(self):
        cadena=self.padre+","+self.madre
        for hijo in self.hijos:
            cadena=cadena+","+hijo
        return cadena
familia1=Familia("Camilo", "Fernanda",["Nicolas", "Tatiana"])
familia2=Familia("Antonio", "Sofia")
familia3=Familia("Luis", "Alba", ["Marcos"])


print(familia1)
print(familia2)
print(familia3)
