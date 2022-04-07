"""
crear un programa que permita cargar 5 nombres de personas y sus respectivas edades. Luego realizar
la carga por tecladode todos los datos a imprimir; los nombres los nombres de las personas mayores de edad
(mayores o iguales a 18 años).
Imprimir la edad promedio de las personas
"""
def cargar_datos():
    nombres=[]
    edades=[]
    for x in range(5):
        v1=input("Ingrese el nombre de la persona: ")
        nombres.append(v1)
        v2=int(input("Ingrese la edad: "))
        edades.append(v2)
    return[nombres, edades]
def mayores_edad(nombres, edades):
    print("Personas mayores de edad:")
    for x in range(len(nombres)):
        if edades[x]>=18:
            print(nombres[x])

def promedio_edades(edades):
    suma=0
    for x in range(len(edades)):
        suma=suma+edades[x]
    promedio=suma//5
    print("Edad promedio pesronas: ", promedio)


#Bloque principal
nombres, edades=cargar_datos()
mayores_edad(nombres, edades)
promedio_edades(edades)
