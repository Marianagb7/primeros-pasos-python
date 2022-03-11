"""
En un curso de 4 estudiantes se registran notas de sus exámenes se requiere:
a) Ingresar nombre y nota de cada estudiante(almacenar los datos en dos listas)
b) Reralizar un listado que muestre los nombres, notas y condición, si la nota es mayor o igual a 8
"Muy buenas notas", "bueno" si la nota esta entre 4 y 7, si la nota es inferior a 4 "insuficiente"
c) Imprimir cuantos estudiantes tiene leyenda muy bueno.
"""
names=[] 
grades = []
for x in range(4):
    name=input("Ingrese el nombre del estudiante: ")
    names.append(name)
    grade=int(input("Ingrese la nota del estudiante: "))
    grades.append(grade)
quantity=0
for x in range(4):
    print(names[x])
    print(grades[x])
    if grades[x]>=8: 
        print("Muy buenas notas")
        quantity=quantity+1
    else:
        if grades[x]>=4:
            print("Bueno")
        else:
            print("Insuficiente")
print("Cantidad de estudiantes con muy buenas notas", quantity)