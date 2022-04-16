"""
crear un diccionario en python para almacenar los datos de funcionarios de una empresa. La clave será su
número de código y en su valor almacenar una lista con el nombre, cargo y salario.
Desarrollar las siguientes funciones:
1. Ingresar datos del funcionario
2. Permitir modificar el sueldo de un empleado. Ingresamos su número de código para buscarlo.
3. Mostrar todos los datos de funcionarios que tienen cargo como "analista sistemas"
"""
def ingresar_datos():
    funcionarios={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el código del funcionario: "))
        nombre=input("Ingrese nombre del funcionario: ")
        cargo=input("Ingrese el cargo: ")
        salario=float(input("Ingrese salario: "))
        funcionarios[codigo]=[nombre, cargo, salario]
        continua=input("Ingresa otro funcionario s/n: ")
    return funcionarios

def imprimir(empleados):
    print("Listado completo de funcionarios")
    for codigo in funcionarios:
        print(codigo, funcionarios[codigo][0], funcionarios[codigo][1], funcionarios[codigo][2])

def modificar_sueldo(funcionarios):
    codigo=int(input("Ingresa el código fel funcionario: "))
    if codigo in funcionarios:
        salario=float(input("Ingresa nuevo salario: "))
        funcionarios[codigo][2]=salario
    else:
        print("No existe funcionario con este código")

def imprimir_analistas(funcionarios):
    print("Listado de \"analista de sistemas\"")
    for codigo in funcionarios:
        if funcionarios[codigo][1]=="analista de sistemas":
            print(codigo, funcionarios[codigo][0], funcionarios[codigo][2])


#Bloque principal
funcionarios=ingresar_datos()
imprimir(funcionarios)
modificar_sueldo(funcionarios)
imprimir(funcionarios)
imprimir_analistas(funcionarios)



