"""
Definir una función que solicite la carga del día, mes, y año. Almacene dichos datos en una tupla que
luego debe retornar. La segunda función debe recibir una tupla con la fecha y mostrar por pantalla.
"""
def cargar_fecha():
    dia=int(input("Ingrese el día: "))
    mes=int(input("Ingrese el mes: "))
    año=int(input("Ingrese el año: "))
    return (dia, mes, año)

def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")

#Bloque principal
fecha=cargar_fecha()
imprimir_fecha(fecha)
lista=list(fecha)
print(lista)
tupla2=tuple(lista)
print(tupla2)

