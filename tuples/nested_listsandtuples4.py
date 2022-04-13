def cargar_candidatos():
    candidatos=[]
    for x in range(3):
        nom=input("Ingrese el nombre del candidato: ")
        cant=int(input("Número de departamentos: "))
        departamentos=[]
        for z in range(cant):
            depart=input("Nombre del departamento: ")
            votos=int(input("Cantidad de votos: "))
            departamentos.append((depart, votos))
        candidatos.append((nom, departamentos))
    return candidatos

def totalvotacion_candidato(candidatos):
    for x in range(len(candidatos)):
        suma=0
        for z in range(len(candidatos[x][1])):
            suma=suma+candidatos[x][1][z][1]
        print(candidatos[x][0], suma)

#Bloque principal
candidatos=cargar_candidatos()
totalvotacion_candidato(candidatos)