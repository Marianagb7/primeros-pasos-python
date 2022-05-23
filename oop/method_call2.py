"""
Plantaer una clase que administre dos lista de 5 nombres de alumno y sus notas. Mostrar un menú
de opciones que permita.
1. Cargar estudiantes
2. Listar estudiantes
3. Mostrar estudiantes con notas mayores o iguales a 7.
4. Finalizar programa
"""
class Estudiantes():
    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1. Ingreso de estudiantes")
            print("2. Listado de estudiantes")
            print("3. Listado de estudiantes con notas mayores o iguales a 7")
            print("4. Finalizar programa")
            opcion=int(input("Ingrese su opción: "))
            if opcion==1:
                self.cargar()
            else:
                if opcion==2:
                    self.listar()
                else:
                    if opcion==3:
                        self.notas_altas()

    def cargar(self):
        for x in range(5):
            nom=input("Ingrese nombre del estudiante: ")
            self.nombres.append(nom)
            nota=int(input("Ingrese la nota: "))
            self.notas.append(nota)
    
    def listar(self):
        print("Listado completo de estudiantes")
        for x in range(5):
            print(self.nombres[x], self.notas[x])
        print("____________________________________________")
    
    def notas_altas(self):
        print("Listado de estudiantes con notas iguales o superiores a 7")
        for x in range(5):
            if self.notas[x]>=7:
                print(self.nombres[x], self.notas[x])
        print("___________________________________________")


estudiantes1=Estudiantes()
estudiantes1.menu()
