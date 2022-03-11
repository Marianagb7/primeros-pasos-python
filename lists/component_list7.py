"""
Crear y cargar por teclado una lista con los nombres de tres estudiantes. Cada estudiante tiene
dos notas almacenar las notas en una lista paralela. Cada componente lista paralela debe ser también 
una lista con las dos notas; imprimir luego cada nombre y sus notas. 
"""
names=[]
grades=[]
for x in range(3):
    name=input("Ingrese el nombre del estudiante: ")
    names.append(name)
    grade1=int(input("Ingrese la primera nota: "))
    grade2=int(input("Ingrese la segunda nota: "))
    grades.append([grade1, grade2])
for x in range(3):
    print(names[x], grades[x][0], grades[x][1])