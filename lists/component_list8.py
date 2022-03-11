names=[]
salaries=[]
totalsalaries=[]
for x in range(3):
    name=input("Ingrese el nombre del empleado: ")
    names.append(name)
    salary1=int(input("Ingrese el primer sueldo: "))
    salary2=int(input("Ingrese el segundo salario: "))
    salary3=int(input("Ingrese tercer salario: "))
    salaries.append([salary1, salary2, salary3])
for x in range(3):
    total=salaries[x][0]+salaries[x][1]+salaries[x][2]
    totalsalaries.append(total)
for x in range(3):
    print(names[x], totalsalaries[x])
posmayor=0
mayor=totalsalaries[0]
for x in range(1, 3):
    if totalsalaries[x]>mayor:
        mayor=totalsalaries[x]
        posmayor=x
print("El empleado con mayor ingresos en los últimos 3 meses")
print(names[posmayor])
print("Con un ingreso mayor:", mayor)