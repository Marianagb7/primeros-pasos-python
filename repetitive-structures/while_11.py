pairs = 0
odd = 0
x = 1
n = int(input("¿Cuantos números vas a ingresar: "))

while x <= n:
    value = int(input("Ingresa los valores: "))
    if value % 2 == 0:
        pairs = pairs + 1
    else:
        odd = odd + 1
    x = x + 1
print("Son pares: ", pairs)
print("Son impares", odd)
