"""
Cargar por teclado y almacenar en una lista, las alturas de 5 personas (valores float).
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas 
más bajas.
"""
height=[]
sum=0
for x in range(5):
    value = float(input("Ingresa la altura: "))
    height.append(value)
    sum = sum + value
print("Las alturas de las personas: ", height)
average = sum/5
print("Promedio de las alturas: ", average)
heigh = 0
lows = 0
for x in range(5):
    if height[x] > average:
        heigh = heigh + 1
    else:
        if height[x]< average:
            lows = lows + 1
print("La cantidad de personas más bajas al promedio", heigh)
print("La cantidad de personas más altas al promedio", lows)
