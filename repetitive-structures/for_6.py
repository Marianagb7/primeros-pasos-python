n = int(input("Cuántos triángulos vas a procesar: "))
quantity = 0

for t in range(n):
    base = int(input("Ingresa el valor de la base del triangulo: "))
    height = int(input("Ingresa el valor de la altura del triangulo: "))
    surface = base * height / 2;
    print("La superficie del triángulo es: ", surface)
    if surface > 12:
        quantity = quantity + 1
print("Cantidad de triángulos con superficie mayor a 12 : ", quantity)