countries=[]
temperatures=[]
averagetem=[]
for x in range(4):
    country=input("Ingrese nombre del país: ")
    countries.append(country)
    temp1=int(input("Ingrese la primera temperatura: "))
    temp2=int(input("Ingrese la segunda temperatura: "))
    temp3=int(input("Ingrese la tercera temperatura: "))
    temperatures.append([temp1, temp2, temp3])
print("Países y temperaturas medias de los últimos tres meses: ")
for x in range(4):
    print(countries[x], temperatures[x][0], temperatures[x][1], temperatures[x][2] )
for x in range(4):
    average=(temperatures[x][0] + temperatures[x][1] + temperatures[x][2])/ 3
    averagetem.append(average)
print("Listado de países y temperaturas medias trimestrales")
for x in range(4):
    print(countries[x], averagetem[x])
posmayor=0
for x in range(1,4):
    if averagetem[x]> averagetem[posmayor]:
        posmayor=x
print("País con temperatura media trimestral mayor", countries[posmayor])

