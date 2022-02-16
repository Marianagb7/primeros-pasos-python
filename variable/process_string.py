"""
Solicitar la carga del nombre de una persona en minúscula. Mostrar un mensaje
si comienza con vocal.
"""
name=input("Ingresar un nombre en minúscula: ")
if name[0]=="a" or name[0]=="e" or name[0]=="i" or name[0]=="o" or name[0]=="u":
    print("El nombre inicia en vocal")
else:
    print("El nombre ingresado no comienza con vocal")