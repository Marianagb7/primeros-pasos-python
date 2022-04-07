"""
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1. Cargar los sueldos en una lista.
2. Impresión de todos los sueldos.
3. Cuántos tienen un sueldo superior a $4.000
4. Retornar el promedio de los sueldos.
5. Mostrar todos los sueldos que estan por denbajo del salario.
"""
def cargar_sueldos():
    sueldos=[]
    for x in range(10):
        sueldo=int(input("Ingrese el sueldo:"))
        sueldos.append(sueldo)
    return sueldos

def imprimir_sueldos(sueldos):
    print("Listado de sueldos: ")
    for x in range(len(sueldos)):
        print(sueldos[x])

def sueldos_mayores4000(sueldos):
    cant=0
    for x in range(len(sueldos)):
        if sueldos[x]>4000:
            cant=cant+1
    print("Cantidad de empleados con sueldo mayor a 4000: ", cant)

def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma=suma+sueldos[x]
    promedio=suma//10
    return promedio

def sueldos_bajos(sueldos):
    pro=promedio(sueldos)
    print("Promedio sueldos empleados")
    print("Sueldos inferiores al promedio: ")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])

#Bloque principal
sueldos=cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayores4000(sueldos)
sueldos_bajos(sueldos)
