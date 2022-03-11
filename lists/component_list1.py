"""
Crear una lista por asignación. La lista tiene que tener cuatro elementos, cada lista debe
ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.
"""
list=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(list)
#Primer componente
print(list[0])
print(list[0][0])
print("-------------")

for x in range(len(list[0])):
    print(list[0][x])
print("------------")

for k in range(len(list)):
    for x in range(len(list[k])):
        print(list[k][x])
