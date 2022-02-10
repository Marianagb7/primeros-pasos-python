multiple_three = 0
multiple_five = 0

for p in range(10):
    value = int(input("Ingrese un valor: "))
    if value % 3 == 0:
        multiple_three = multiple_three + 1
    if value % 5 == 0:
        multiple_five = multiple_five + 1
print("Cantidad de valores múltiplos de 3: ", multiple_three)
print("Cantidad de valores múltiplos de 5: ", multiple_five)


    
