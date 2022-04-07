"""
Confeccionar una aplicación que muestre una presentación en pantalla del programa, que solicite la carga
de dos valores y nos muestre la suma.
Finalmente mostrar un mensaje de despedidad del programa.
"""
def mostrar_mensaje(mensaje):
    print("***********************************************")
    print(mensaje)
    print("************************************************")

def cargar_suma():
    valor1=int(input("Ingrese primer valor: "))
    valor2=int(input("Ingrese segundo valor: "))
    suma=valor1+valor2
    print("La suma de los valores es: ", suma)
#Bloque principal
mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado")
cargar_suma()
mostrar_mensaje("Gracias por utilizar este programa")
