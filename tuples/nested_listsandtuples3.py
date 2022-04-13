def carga_empleados():
    empleados=[]
    for x in range(5):
        nom=input("Ingrese nombre del trabajador: ")
        suel1=int(input("Ingrese primer salario: "))
        suel2=int(input("Ingrese segundo salario: "))
        suel3=int(input("Ingrese tercer salario: "))
        empleados.append([nom, (suel1, suel2, suel3)])
    return empleados

def ganancias(empleados):
    print("Monto total ganado por el empleado en los últimos tres meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0], total)

def ganancias_superior10000(empleados):
    print ("Empleados con ingresos superiores a 10000 en los últimos 3 meses: ")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0], total)

#Bloque principal
empleados=carga_empleados()
ganancias(empleados)
ganancias_superior10000(empleados)
