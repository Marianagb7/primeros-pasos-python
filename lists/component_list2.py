"""
Crear una lista por asignación.
La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenidad en la lista principal.
"""
list=[[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]
add1=list[0][0]+list[0][1]+list[0][2]+list[0][3]+list[0][4]
add2=list[1][0]+list[1][1]+list[1][2]+list[1][3]+list[1][4]
print(add1)
print(add2)
print("------------")
add1=0
for x in range(len(list[0])):
    add1=add1+list[0][x]
add2=0
for x in range(len(list[1])):
    add2=add2+list[1][x]
print(add1)
print(add2)
print("-----------")

for k in range(len(list)):
    add=0
    for x in range(len(list[k])):
        add=add+list[k][x]
        print(add)
