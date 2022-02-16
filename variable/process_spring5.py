"""
Ingresar una oraciónque pueda tener letras tanto en mayúscula como en minúscula.
Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúscula para que sea más facíl dispner la 
condición que verifica que es una vocal.
"""
sentence=input("Ingrese una oración: ")
lower_sentece=sentence.lower()
quantity=0
x=0
while x<len(lower_sentece):
    if sentence[x]=="a" or sentence[x]=="e" or sentence[x]=="i" or sentence[x]=="o" or sentence[x]=="u":
        quantity=quantity+1
    x=x+1
print("La cantidad de vocales de la oración es: ", quantity)