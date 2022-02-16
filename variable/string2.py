"""
Crear un programa donde el usuario ingrese dos nombres por teclado.
Mostrar cuál de los dos es mayor alfabeticamente o si son iguales.
"""
name1 = input("Ingresa primer nombre: ")
name2 = input("Ingrese segundo nombre: ")
if name1 == name2:
    print("Ingreso dos nombres iguales")
else:
    if name1 > name2:
       print(name1, "Es mayor alfabeticamente")
    else:
        print(name2, "Es mayor alfabeticamente")
