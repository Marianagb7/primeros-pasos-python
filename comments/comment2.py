"""
Realizar un programa que solicite la carga de valores enteros
por teclado y los sume. Finalizar la carga al ingresar el valor -1.
"""
sum = 0
value = int(input("Ingresar valor (-1 finaliza la carga): ")) #se carga el primer valor
while value != -1:
    sum =sum + value
    value = int(input("Ingresa valor (-1 finaliza la carga): "))#se carga desde el segundo valor hasta el último valor
print("Suma valores ingresados", sum)