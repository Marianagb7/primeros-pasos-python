"""
Definir una lista que almacene por asignación  los nombres de 5 personas.
Contar cuántos de esos nombres tienen 5 carácteres.
"""
names=["Karina", "Laura", "María", "Luna", "Tatiana"]
amount=0
x=0
while x<len(names) :
    if len(names[x])>=5:
        amount=amount+1
    x=x+1
print("Listado de nombres", names)
print("Cantidad de nombres con 5 carácteres o más", amount)