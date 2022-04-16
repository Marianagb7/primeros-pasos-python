"""
Confeccionar un programa con las siguientes funciones:
1. Cargar una lista con 5 palabras.
2. intercambiar la primera palabra con última
3. Imprimir la lista
"""
def cargar():
    palabras=[]
    for x in range(5):
        pal=input("Ingrese una palabra:")
        palabras.append(pal)
    return palabras

def intercambiar(palabras):
    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux

def imprimir(palabras):
    print(palabras)

#Bloque principal
palabras=cargar()
imprimir(palabras)
intercambiar(palabras)
imprimir(palabras)
