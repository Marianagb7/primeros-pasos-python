"""
Ingrese por teclado el nombre, edad, altura de dos personas.
Mostrar por pantalla la persona con mayor altura
"""
print("Datos persona 1")

name1=input("Ingrese nombre: ")
age1=int(input("Ingrese edad: "))
height1=float(input("Ingrese estatura: "))

print("Datos persona 2")

name2=input("Ingrese nombre: ")
age2=int(input("Ingrese edad: "))
height2=float(input("Ingrese estatura: "))
print("Persona más alta")
if height1 > height2:
    print(name1)
else:
    print(name2)