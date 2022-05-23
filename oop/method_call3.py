"""
Debe mostrar un menú con las siguientes opciones:
1. Cargar un contacto en la agenda.
2. Listado completo de la agenda.
3. Consulta ingresando el nombre de la persona.
4. Modificación de su teléfono y mail.
5. Finalizar programa
"""
class Agenda:
    def __init__(self):
        self.contactos={}

    def menu(self):
        opcion=0
        while opcion !=5:
            print("1.Carga de un contacto en la agenda: ")
            print("2. Listado completo agenda")
            print("3. Consulta ingresando el nombre de la persona: ")
            print("4. Modificación del teléfono y mail")
            print("5. Finalizar programa")
            opcion=int(input("Ingrese su opción: "))
            if opcion==1:
                self.cargar()
            else:
                if opcion==2:
                    self.listado()
                else:
                    if opcion==3:
                        self.consulta()
                    else:
                        if opcion==4:
                            self.modificacion()

    def cargar(self):
        nombre=input("Nombre de la persona: ")
        telefono=input("Teléfono: ")
        mail=input("Email: ")
        self.contactos[nombre]=(telefono, mail)
        print("_________________________________")

    def listado(self):
        print("Listado de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0], self.contactos[nombre][1])
        print("______________________________")

    def consulta(self):
        nombre=input("Ingrese el nombre de la persona a consultar: ")
        if nombre in self.contactos:
            print(nombre, "su teléfono es:", self.contactos[nombre][0], "su email es: ", self.contactos[nombre][1])
        else:
            print("No existe contacto con este nombre")
        print("___________________________________")
    
    def modificacion(self):
        nombre=input("Ingrese el nombre de la persona para modificar teléfono y email: ")
        if nombre in self.contactos:
            telefono=input("Ingrese nuevo teléfono: ")
            mail=input("Ingrese nuevo email: ")
            self.contactos[nombre]=(telefono, mail)
        else:
            print("No existe un contacto con ese nombre")

#Bloque principal
agenda1=Agenda()
agenda1.menu()