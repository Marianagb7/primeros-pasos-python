"""
Crear y cargar en una lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes.
Ordenar alfabéticamente e imprimir los resultados. Por ultimo oredenar con respecto a la cantidad
de habitantes(de mayor a menor)e imprimir nuevamente.
"""
countries=[]
population=[]
for x in range(5):
    name=input("Ingrese el nombre del país: ")
    countries.append(name)
    quantity=int(input("Cantidad de habitantes: "))
    population.append(quantity)
# Ordenamiento alfabético
for k in range(4):
    for x in range(4-k):
        if countries[x]>countries[x+1]:
            aux1=countries[x]
            countries[x]=countries[x+1]
            countries[x+1]=aux1
            aux2=population[x]
            population[x]=population[x+1]
            population[x+1]=aux2
print("Listado países orden alfabético")
for x in range(5):
    print(countries[x], population[x])

# Ordenamiento por cantidad de habitantes
for k in range(4):
    for x in range(4-k): 
        if population[x]<population[x+1]:
            aux1= countries[x]
            countries[x]=countries[x+1]
            countries[x+1]=aux1
            aux2=population[x]
            population[x]=population[x+1]
            population[x+1]=aux2
print("Listado de países por cantidad de habitantes")
for x in range(5):
    print(countries[x], population[x])
