# Crear una lista y almacenar los nombres de 5 paises. Ordenar alfabéticamente la lista e imprimirla.

countries= []
for x in range(5):
    country=input("Ingrese el nombre del país: ")
    countries.append(country)
print("Lista sin ordenar",countries)
#Ordenamiento
for k in range(4):
    for x in range(4-k):
        if countries[x]>countries[x+1]:
            aux=countries[x]
            countries[x]=countries[x+1]
            countries[x+1]=aux
print("Listado de paises ordenada", countries)
