"""
Realizar la carga de valores enteros por teclado, almacenarlos en una lista.Finalizar la carga
de elemntos al ingresar el cero. Mostrar finalmente el tamaño de la lista y el contenido de la 
lista.
"""
list =[]
value = int(input("Ingresar un valor(0 para finalizar): "))
while value!= 0 :
    list.append(value)
    value=int(input("Ingresa un valor(0 para finalizar): "))
print("Contenido lista", list)
print("Tamaño lista", len(list))
