add1 = 0
add2 = 0
add3 = 0
for f in range(5):
    age = int(input("Ingresar edad: "))
    add1 = add1 + age
average1= add1 / 5
print("Promedio de edades turno mañana ", average1)
for f in range(6):
    age = int(input("Ingresar edad: "))
    add2 = add2 + age
average2 = add2 / 6
print("Promedio de edades turno tarde", average2)
for f in range(11):
    age = int(input("Ingresar edad: "))
    add3 = add3 + age
average3= add3 / 11
print("Promedio de edades turno noche: ", average3)
if average1 < average2 and average1 < average3:
    print("El turno de la mañana tiene un promedio de edades menor")
else:
    if average2 < average3:
       print("El turno de la tarde tiene un promedio de edades menor:  ")
    else:
        print("El turno de la noche tiene un promedio de edades menor")


