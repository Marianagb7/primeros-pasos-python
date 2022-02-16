"""
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres.
Controlar que el string tenga 10 y 20 caracteres para que sea valido en caso contrario mostrar
un mensaje de error.
"""
password=input("Ingrese una clave que tenga entre 10 y 20 caracteres: ")

if len(password)>=10 and len(password)<=20:
    print("Largo correcto")
else:
    print("Largo incorrecto")