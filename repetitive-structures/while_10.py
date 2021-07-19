equal_one = 0
equal_two = 0
x = 1

while x <= 15:
    value = int(input("Ingresa una lista de 15 números: "))
    equal_one = equal_one + value
    x = x + 1
x = 1
while x <= 15:
    value = int (input("Ingresa una segunda lista de 15 valores: "))
    equal_two = equal_two + value
    x = x + 1
if equal_one > equal_two:
    print("Lista 1 mayor")
else:
    if equal_two > equal_one:
        print("Lista 2 mayor")
    else:
        print("Listas iguales")
