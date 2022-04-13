"""
Definir una función  que cargue una lista con palabras y las retorne.
Luego otra función tiene que mostrar todas las palabaras de la lista más de 5 carácteres.
"""
def cargar():
    palabras=[]
    cant=int(input("¿Cuántas palabras quiere ingresar?"))
    for x in range(cant):
        pal=input("Ingrese la palabra: ")
        palabras.append(pal)
    return palabras

def palabras_mas5(palabras):
    print("Palabras ingresadas con más de 5 carácteres: ")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra)

#Bloque principal
palabras=cargar()
palabras_mas5(palabras)