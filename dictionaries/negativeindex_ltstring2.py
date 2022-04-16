"""
Ingresar una cadena de carácteres por teclado. Mostrar la cadena al final, al principio utilizando
subindes negativos.
"""
palabra=input("Ingrese una palabra: ")
indice=-1
for x in range(len(palabra)):
    print(palabra[indice], end="")
    indice=indice-1
    