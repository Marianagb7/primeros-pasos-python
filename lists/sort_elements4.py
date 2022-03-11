"""
Solicitar por teclado la cantidad de empleados que tiene la empresa.
Crear y cargar una lista con todos los sueldos de los empleados. Imprimir la lista de sueldos
ordenados de menor a mayor.
"""
salaries=[]
quantity=int(input("Cuántos empleados tiene la empresa: "))
for x in range(quantity):
    salary=int(input("Ingrese el sueldo: "))
    salaries.append(salary)
#Ordenamiento lista
for k in range(quantity-1):
    for x in range(quantity-1-k):
        if salaries[x]>salaries[x+1]:
            aux=salaries[x]
            salaries[x]=salaries[x+1]
            salaries[x+1]=aux
print("Listado de salarios ordenados", salaries)