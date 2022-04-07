"""
Desarrollar una función que reciba un string y nos retorne el que tiene más caracteres. Si hay más de uno
con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más bajo.
En el bloque principal iniciamos por asignación la lista de string.
"""
def mascaracteres(lista):
    pos=0
    for x in range(1, len(lista)):
        if len(lista[x])>len(lista[pos]):
            pos=x
    return lista[pos]
#Bloque principal
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print(palabras)
print("Palabras con más caracteres: ", mascaracteres(palabras))