#Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar la suma de ellos.

list = [10, 20, 30, 40, 50]
sum = 0
x =0
while x<len(list):
    sum = sum + list[x]
    x=x+1
print("Los elementos de la lista son : ", list)
print("La suma de la lista es: ", sum)