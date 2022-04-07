"""
Construir un programa que muestre una presentación en pantalla del programa. Solicite la carga de dos valores
y nos muestre la suma.
Mostrar finalmente un mensaje de despedida del programa.
Implementar estas actividades en tres funciones. 
"""
def presentacion():
    print("Programa que permite cargar por teclado valores")
    print("Efectuar la suma de dos valores")
    print("************************************")

def carga_suma():
    valor1=int(input("Ingresa el primer valor:"))
    valor2=int(input("Ingresa segundo valor: "))
    suma=valor1+valor2
    print("La suma de dos valores es : ", suma)

def finalizacion():
    print("****************************")
    print("Gracias por utilizar este programa")

# Bloque principal del programa
presentacion()
carga_suma()
finalizacion()