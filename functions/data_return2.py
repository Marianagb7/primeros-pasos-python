
# Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
def retornar_mayor(v1, v2):
    if v1>v2:
        return v1
    else:
        return v2
# Bloque principal
valor1=int(input("Ingresar primer valor: "))
valor2=int(input("Ingresar segundo valor: "))
mayor=retornar_mayor(valor1, valor2)
print(mayor)