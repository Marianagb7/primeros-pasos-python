"""
Confeccionar una palicación que solicite la carga de dos valoresenteros y muestre su suma.
Repetir la carga e impresión de la suma 5 veces.
Mostrar una linea separada después que cargamos valores y suma.
"""
def carga_suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese segundo valor: "))
    suma=valor1+valor2
    print("La suma de los dos valores es", suma)
def separacion():
    print("**************")

#Bloque principal
for x in range(5):
    carga_suma()
    separacion()