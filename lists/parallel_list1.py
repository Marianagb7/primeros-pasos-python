"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus respectivas edades.
Luego de realizar la carga por teclado de todos los datos, imprimir los nombres de las personas mayores 
de edad(mayor o iguales a 18 años)
"""
names=[]
ages=[]
for x in range(5):
    name=input("Ingrese nombre de la persona: ")
    names.append(name)
    age=int(input("Ingrese la edad de la persona: "))
    ages.append(age)
print("Lista de personas mayores de edad: ")
for x in range(5):
    if ages[x]>=18:
        print(names[x])

