"""
Almacenar en una lista los sueldos(valores float) de 5 operarios. 
Imprimir la lista y el promedio de sueldos.
"""
salary =[]
add=0
for x in range(5):
    value=float(input("Ingrese el sueldo del operario: "))
    salary.append(value)
    add=add+value
print("Lista de sueltos", salary)
average=add/5
print("Promedio de sueldos", average)