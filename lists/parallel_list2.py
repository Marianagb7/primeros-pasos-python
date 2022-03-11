"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra.
Definir dos listas paralelas. MOstrar cuántos productos tienen un precio mayor al primer 
producto ingresado.
"""
products = []
prices = []

for x in range(5):
    product=input("Ingrese el nombre del producto: ")
    products.append(product)
    price=int(input("Ingrese el precio del proyecto: "))
    prices.append(price)
quantity=0
for x in range(1,5):
    if prices[x]>prices[0]:
        quantity=quantity+1
print("Cantidad de productos con precio mayor al primer producto ingresado",quantity)
