"""
Realizar la carga de dos nombres de personas distintos.Mostrar por 
pantalla, luego ordenarlos en forma alfabética.
"""
name1=input("Ingresa primer nombre: ")
name2=input("Ingresa segundo nombre: ")
print("Listado en orden alfabetico")
if name1<name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
