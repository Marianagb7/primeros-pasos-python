"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
Mostrar el nombre de la persona de menor orden alfabético. 
"""
names = []
for x in range(5):
    nam = input("Ingrese nombre de la persona: ")
    names.append(nam)
    shortname=names[0]
for x in range(1,5):
    if names[x]<shortname:
        shortname=names[x]
print("Lista completa de nombres",names)
print("Nombre menor en orden alfabético", shortname)