top = 0
low = 0
x = 1

while x <= 10:
    score = int(input("Ingrese la notas: "))
    if score >= 7:
       top = top + 1
    else:
        low = low + 1
    x = x + 1
print("Cantidad de estudiantes con notas iguales o inferiores a 7: ")
print(top)
print("Cantidad de estudiantes con notas inferiores a 7: ")
print(low)
