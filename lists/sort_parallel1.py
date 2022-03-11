"""
Crear un programa que permita cargar los nombres de 5 estudiantes y sus notas respectivas.
Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.
"""
from turtle import st


students=[]
grades=[]
for x in range(5):
    name=input("Ingrese el nombre del estudiante: ")
    students.append(name)
    grade=int(input("Ingrese la nota del estudiante: "))
    grades.append(grade)
#Ordenamiento
for k in range(4):
    for x in range(4-k):
        if grades[x]<grades[x+1]:
            aux1=grades[x]
            grades[x]=grades[x+1]
            grades[x+1]=aux1
            aux2=students[x]
            students[x]=students[x+1]
            students[x+1]=aux2
print("Lista de estudiantes y sus notas ordenadas de mayor a menor")
for x in range(5):
    print(students[x], grades[x])