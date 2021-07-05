num1= int(input("Ingresa el primer número: "))
num2= int(input("Ingresa el segundo número: "))
num3= int(input("Ingresa el tercer número: "))
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

