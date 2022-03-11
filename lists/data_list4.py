"""
Definir por asignación una lista con 8 elementos enteros. Contar cuántos de dichos valores almacenan
un valor superior a 100
"""
list=[10, 567, 333, 445, 12, 56, 78, 23]
amount=0
x=0
while x<len(list):
    if list[x]>100:
        amount=amount+1
    x= x+1
print("Los valores de la lista son: ", list)
print("Cantidad de valores mayores a 100 que se encuentran en la lista: ", amount)

        
