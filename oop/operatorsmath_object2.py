"""
Desarrollar una clase llamada lista que permita pasar al método init. Una lista de valores enteros.
Redefinir el operador +.
"""
class Lista:

    def __init__(self, lista):
        self.lista=lista

    def imprimir(self):
        print(self.lista)

    def __add__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva
lista1=Lista([2, 3, 1])
lista1.imprimir()
print(lista1+10)
lista2=lista1+30
print(lista2)

