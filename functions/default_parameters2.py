"""
Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos
valores. Debe tener tres parámetros por defecto.
"""

def sumar(v1, v2, v3=0, v4=0, v5=0):
    s= v1+v2+v3+v4+v5
    return s
#bloque principal
print("La suma de 5 + 6=", sumar(5, 6))
print("Lasuma de 5 + 6 +3=", sumar(5, 6, 3))
print("La suma de 1 + 1 + 1 + 1=", sumar(1, 1, 1, 1))
print("La suma de 1 + 1 + 1 + 1 + 1=", sumar(1, 1, 1, 1, 1))