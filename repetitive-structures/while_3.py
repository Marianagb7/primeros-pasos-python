x = 1
addition = 0

while x<= 10:
    value = int(input("Ingresa diez valores: "))
    addition = addition + value
    x = x + 1
average = addition//10
print("La suma de los valores es: ")
print(addition)
print("El promedio de los valores es: ")
print(average)