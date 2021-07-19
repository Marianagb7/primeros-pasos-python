quantity = 0
x = 1
n = int(input("¿cuántas piezas cargara?: "))
while x<=n:
    length = float(input("Ingrese la medida de la pieza:  "))
    if length>=1.2 and length<=1.3:
        quantity = quantity+1
    x=x+1
print("Las piezas aptas son: ") 
print(quantity)