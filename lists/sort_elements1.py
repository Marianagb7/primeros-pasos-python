"""
Crear y cargar una lista con cinco salarios.Desplazar el valor mavor de la lista a la última
posición.
"""
salaries =[]
for x in range(5):
    value=int(input("Ingrese el salario: "))
    salaries.append(value)
print("Lista original", salaries)
for x in range(4):
    if salaries[x]>salaries[x+1]:
        aux=salaries[x]
        salaries[x]=salaries[x+1]
        salaries[x+1]=aux
print("Lista ordenada",salaries)