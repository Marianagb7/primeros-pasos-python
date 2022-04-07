"""
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los
valores hacerlo por teclado en otra función.
"""
def mostrar_mayor(v1, v2, v3):
    print("El valor mayor de los tres números es: " )
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)
def cargar():
    valor1=int(input("Ingresa el primer valor: "))
    valor2=int(input("Ingrese segundo valor: "))
    valor3=int(input("Ingrese tercer valor: "))
    mostrar_mayor(valor1, valor2, valor3)

#Bloque principal
cargar()
    