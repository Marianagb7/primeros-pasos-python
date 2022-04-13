"""
Crear un programa con las siguientes funciones:
1. Cargar el nombre del trabajador y su sueldo. Retornar una tupla con dichos valores.
2. Una función que reciba como párametro dos tuplas con los nombres y sueldos de empleados.
Muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y segudamente llamar
a la función que muestra el nombre de empleado con sueldo mayor.
"""
def cargar_empleado():
    nombre=input("Ingrese nombre del empleado: ")
    sueldo=float(input("Ingrese el sueldo: "))
    return(nombre, sueldo)

def mayor_sueldo(empleado1, empleado2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0], "Tiene el mayor sueldo")
    else:
        print(empleado2[0], "Tiene mayor sueldo")

#Bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1, empleado2)