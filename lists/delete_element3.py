employees=[]
salaries=[]
number=int(input("Cuántos empleos tiene la empresa: "))
for x in range(number):
    name=input("Nombre del empleado: ")
    employees.append(name)
    salary=int(input("Ingrese el monto del salario: "))
    salaries.append(salary)
print("Listado completo de empleados")
for x in range(len(salaries)):
    print(employees[x], salaries[x])
position=0
while position < len(salaries):
    if salaries[position]>10000:
        salaries.pop(position)
        employees.pop(position)
    else:
        position=position+1
print ("Listado de empleados que devengan 10.000 o menos")
for x in range(len(salaries)):
    print(employees[x], salaries[x])