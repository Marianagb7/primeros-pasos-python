negative = 0
positive = 0
multiple15 = 0
sum_even = 0
for f in range(10):
    value=int(input("Ingrese valor: "))
    if value <0:
        negative=negative+1
    else:
        if value>0:
            positive=positive+1
    if value % 15 ==0:
        multiple15=multiple15+1
    if value % 2 == 0:
        sum_even= sum_even+value
print("Cantidad valores negativos")
print(negative)
print("Cantidad de valores positivos")
print(positive)
print("Cantidad de multiplos de 15")
print(multiple15)
print("Suma de valores ingresados")
print(sum_even)

