"""
Realizar la carga de enteros por teclado.Preguntar después de ingresado el valor,
si desea cargar otro valor, responder si o no por teclado.
Mostrar la suma de los valores ingresados.
"""
sum=0
option="si"
while option == "si":
    value=int(input("Ingresa un valor: "))
    sum=sum+value
    option=input("Desea cargar otro valor (si/no): ")
print("La suma de los valores ingresados es: ",sum)