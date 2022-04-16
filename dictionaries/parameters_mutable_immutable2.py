"""
Confeccionar un programa que contenga las siguientes funciones:
1. Carga una lista de 5 nombres.
2. Ordenar alfabeticamente la lista.
3. Imprimir la lista de nombres
"""
def cargar():
    nombres=[]
    for x in range(5):
        nom=input("Ingrese nombre: ")
        nombres.append(nom)
    return nombres

def ordenar(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux=nombres[x]
                nombres[x]=nombres[x+1]
                nombres[x+1]=aux
    
def imprimir(nombres):
    for nombre in nombres:
        print(nombre)

#Bloque principal
nombres=cargar()
print("Imprimimos antes de ordenar")
imprimir(nombres)
ordenar(nombres)
print("Imprimir después de ordenar")
imprimir(nombres)
