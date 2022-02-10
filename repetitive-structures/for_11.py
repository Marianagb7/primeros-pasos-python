coordinate1 = 0
coordinate2 = 0
coordinate3 = 0
coordinate4 = 0
p = int(input("Ingrese la cantidad de puntos: "))
for m in range(p):
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))
    if x > 0 and y > 0:
        coordinate1 = coordinate1 + 1
    else:
        if x < 0 and y > 0 :
            coordinate2 = coordinate2 + 1
        else:
            if x < 0 and y < 0:
                coordinate3 = coordinate3 +1
            else:
                if x>0 and y < 0:
                    coordinate4 = coordinate4 + 1
print("Cantidad de puntos ingresados primer cuadrante: ", coordinate1)
print("Cantidad de puntos ingresados segundo cuadrante: ", coordinate2)
print("Cantidad de puntos ingresados tercer cuadrante: ", coordinate3)
print("Cantidad de puntos ingresados cuarto cuadrante: ", coordinate4)