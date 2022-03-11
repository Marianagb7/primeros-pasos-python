employees=[]
adsences=[]
for k in range(3):
    name=input("Ingrese el nombre del trabajador: ")
    employees.append(name)
    quantity=int(input("Cuántos días inasistió: "))
    adsences.append([])
    for x in range(quantity):
        day=int(input("Ingrese el día del mes de la inesistencia: "))
        adsences[k].append(day)
print("Nombre de empleados y días de inasistencia")
for k in range(3):
    print(employees[k])
    for x in range(len(adsences[k])):
        print(adsences[k][x])
print ("Nombre del empleado y cantidad de inasistencias ")
for x in range(3):
    print(employees[x], len(adsences[x]))
men = len(adsences[0])
for x in range(1,3):
    if len(adsences[x])<men:
        men=len(adsences[x])
print("Trabajador o trabajadores que faltarón menos")
for x in range(3):
    if len(adsences[x]) == men:
        print(employees[x])
