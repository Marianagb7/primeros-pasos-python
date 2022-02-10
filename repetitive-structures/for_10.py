quantity1 = 0
quantity2 = 0
quantity3 = 0
n = int(input("Ingresa la cantidad de triangulos: "))
for t in range(n):
    side1 = int(input("Ingresa el valor del lado 1: "))
    side2 = int(input("Ingresa el valor del lado 2: "))
    side3 = int(input("Ingresa el valor del lado 3: "))
    if side1 ==side2 and side1 == side3:
        print("Es un triángulo equilátero")
        quantity1= quantity1 + 1
    else:
        if side1 == side2 or side1 == side3 or side2 == side3:
            print("Es un triángulo isósceles")
            quantity2 = quantity2 + 1
        else:
            print("Es un triángulo escaleno")
            quantity3 = quantity3 + 1
print("La cantidad de triángulos equiláteros es: ", quantity1)
print("La cantidad de triángulos isósceles es: ", quantity2)
print("La cnatidad de triángulos escalenos es: ", quantity3)