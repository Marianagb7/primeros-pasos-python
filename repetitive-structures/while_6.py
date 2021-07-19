addition = 0
x = 1
n = int(input("¿Cuántas personas va a procesar?: "))
while x <= n:
     tall = float(input("Ingresa la altura de las personas: "))
     addition = addition + tall
     x = x + 1
average = addition / n
print("El promedio de estatura de las personas es: ")
print(average)