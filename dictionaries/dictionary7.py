"""
Crear un programa que almacene los datos de 3 estudiantes. Definir un diccionario conde la clave 
sea el número de documento de identificación del estudiante. Como valor almacenar en una lista  con
componentes de tipo tupla donde almacenaremos nombre de las materias y su nota.
Crear las siguientes funciones:
1. Cargar estudiantes(identificación)
2. Listado de todos los alumnos con sus notas
3. consulta un estudiante por identificación(mostrar materias que cursa y notas) 
"""
def cargar():
    alumnos={}
    for x in range(3):
        identificacion=int(input("Ingrese número de identificación del estudiante: "))
        listamaterias=[]
        continua="s"
        while continua=="s":
            materia=input("Ingrese nombre de la materia: ")
            nota=float(input("Ingrese la nota: "))
            listamaterias.append((materia, nota))
            continua=input("Ingresa otra materia s/n: ")
        alumnos[identificacion]=listamaterias
    return alumnos

def listar(alumnos):
    print("Listado completo de estudiantes y sus notas por materia")
    for identificacion in alumnos:
        print("Identificación del estudiante ", identificacion)
        print("Materias que cursa y sus notas")
        for materia, nota in alumnos[identificacion]:
            print(materia, nota)

def consulta_notas(alumnos):
    identificacion=int(input("Ingresa la identificación a consultar: "))
    if identificacion in alumnos:
        for materia, nota in alumnos[identificacion]:
            print(materia, nota)

#Bloque principal
alumnos=cargar()
listar(alumnos)
consulta_notas(alumnos)


            