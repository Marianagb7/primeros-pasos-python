"""
Crear una función que le enviemos un número de mes como parámetro y nos retorne una tupla con todos los 
nombres de meses que faltan hasta fin de año.
"""
def meses_faltantes(numeromes):
    meses=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
    "septiembre", "octubre", "noviembre", "diciembre")
    return meses[numeromes:]
#Bloque principal
numeromes=int(input("Ingresar el número de mes:"))
meses_faltantes=meses_faltantes(numeromes)
print("Nombre de meses que faltan hasta fin de año")
print(meses_faltantes)