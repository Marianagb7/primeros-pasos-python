parents=[]
children=[]
for k in range(3):
    father=input("Ingrese el nombre del padre: ")
    mother=input("Ingrese nombre de la madre: ")
    parents.append([father, mother])
    quantity=int(input("Cuántos hijos tienen: "))
    children.append( [] )
    for x in range(quantity):
        name=input("Ingrese nombre de la hija o hijo: ")
        children[k].append(name)
print("Listado del padre, madre y sus hijos")
for k in range(3):
    print("Padre: ", parents[k][0])
    print("Madre: ", parents[k][1])
    for x in range(len(children[k])):
        print("Hijo: ", children[k][x])
print("Listado padres y cantidad de hijos")
for x in range(3):
    print("Padre", parents[x][0])
    print("Cantidad de hijos", len(children[x]))