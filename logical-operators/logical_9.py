num1 =int(input("Ingresa el primer número entero: "))
num2 =int(input("Ingresa el segundo número entero: "))
num3 =int(input("Ingresa el tercer número entero: "))

if num1<num2 and num1<num3:
    print(num1)
else:
    if num2<num3:
        print(num2)
    else:
        print(num3)
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)