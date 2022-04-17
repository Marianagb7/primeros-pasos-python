"""
Crear un programa que genere un número aleatorio entre 1 y 100. Que no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje"Felicitaciones ganaste"; si el número es igual
al generado o "intenta de nuevo el número es mayor" 0  intenta de nuevo el número es menor".
Mostrar cuando gana cuantos intentos necesito.
"""
import random

print("Intente adivinar el número entre 1 y 100")
aleatorio=random.randint(1, 100)
intentos=0
elegido=-1
while elegido != aleatorio:
    elegido=int(input("Elige un número: "))
    if aleatorio < elegido:
        print("Intenta de nuevo el número es mayor")
    else:
        if aleatorio > elegido:
            print("Intente de nuevo el número es menor")
    intentos=intentos +1
print("Felicitaciones ganaste", intentos, "intentos")