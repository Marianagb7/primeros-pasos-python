quantity = 0
n = int(input("Cuántos valores vas a ingresar:  "))
for f in range(n):
    value = int(input("Ingresa el valor: "))
    if value >= 1000:
        quantity = quantity + 1
print("Cantidad de valores mayores o iguales a 1.000: ", quantity)
    