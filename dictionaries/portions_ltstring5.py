"""
Cargar una cadena por teclado luego:
1. Imprimir los dos primeros carácteres.
2. Imprimir los dos últimos.
3. Imprimir todos menos el primero y el último caracter.
"""
cadena=input("Ingrese una cadena de carácteres: ")
print("Primeros dos carácters")
print(cadena[:2])
print("Los dos últimos carácteres")
print(cadena[len(cadena)-2:])
print("Imprimir todos los carácteres menos el primero y el último")
print(cadena[1:len(cadena)-1])
