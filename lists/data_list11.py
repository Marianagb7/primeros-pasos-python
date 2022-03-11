"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde).
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""
morning = []
print("Salarios del turno de la mañana")
for x in range(4):
    value = float(input("Ingrese salario: "))
    morning.append(value)
print("Salarios turno de la tarde")
afternoon=[]
for x in range(4):
    value = float(input("Ingrese salario: "))
    afternoon.append(value)
print("Turno de la mañana", morning)
print("Turno de la mañana", afternoon)
