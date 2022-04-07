#Elaborar una función que reciba tres enteros y nosretorne el valor promedio de los mismos.
def retornar_promedio(v1, v2, v3):
    promedio=(v1+v2+v3)/3
    return promedio
#Bloque principal
valor1=int(input("Ingresar primer valor: "))
valor2=int(input("Ingresar segundo valor: "))
valor3=int(input("Ingresar tercer valor: "))
print("Valor promedio de los tres valores ingresados es: ", retornar_promedio(valor1, valor2, valor3))
