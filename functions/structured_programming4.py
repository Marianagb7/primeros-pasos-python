"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal
del programa llamar 2 veces dicha función.(Sin usar una estructura repetitiva)
"""
def menor_valor():
    valor1=int(input("Ingresar primer valor: "))
    valor2=int(input("Ingresar segundo valor: "))
    valor3=int(input("Ingresar tercer valor: "))
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)
#Bloque principal
menor_valor()
menor_valor()