"""
Definir una tupla con tres valores enteros. Convertir el contenido de tupla a tipo lista.
Modificar la lista y luego convertir la lista en tupla.
Crear otra tupla a partir de tres variables independiente que almacene el día, mes y año.(empaquetamiento),
luego desempaquetar la tupla a otras tres variables independientes.
"""
from string import octdigits


fechatupla1=(1, 5, 2022)
print("Imprimir la tupla")
print(fechatupla1)
fechalista1=list(fechatupla1)
print("Imprimimos la lista que se copio de la tupla")
print(fechalista1)
fechalista1[0]=25
print("Imprimimos la lista modificada")
print(fechalista1)
fechatupla2=tuple(fechalista1)
print("Imprimir la segunda tupla que se le copio la lista")
print(fechatupla2)

dia=10
mes=5
año=2022
fechatupla3=dia, mes, año
print(fechatupla3)
dia1, mes1, año1 = fechatupla3
print(dia1, mes1, año1)