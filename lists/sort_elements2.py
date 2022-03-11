# Crear y cargar una lista con 5 salarios y ordenarlos de mayor a menor.

salaries = []
for x in range(5):
    value=int(input("Ingresar salario: "))
    salaries.append(value)
print("Lista sin ordenar", salaries)
# ordenamiento
for k in range(4):
    for x in range(4):
        if salaries[x]>salaries[x+1]:
            aux = salaries[x]
            salaries[x]=salaries[x+1]
            salaries[x+1]=aux
print("Lista ordenada", salaries)

