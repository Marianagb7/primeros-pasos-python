"""
Cargar una oración por teclado. Mostrar cuantos espacios en blanco se ingresaron.
Tener en cuenta que espacio en blanco es igual a " ", en cambio una cadena vacia es ""
"""
sentence=input("Escribe una oración: ")
quantity=0
x=0
while x<len(sentence):
    if sentence[x]== " ":
        quantity=quantity+1
    x=x+1
print("La cantidad de espacios ingresados es ", quantity)
