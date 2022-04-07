"""
Crear una función que llegue como primer parámetro el nombre del empleado, como segundo parámetro el costo
por hora y finalmente la cantidad de horas trabajadas.
Llmar a dicha función empleando la carasterística de python de argumentos nombrados.
"""
def calcular_sueldo(nombre, costohora, cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre, "trabajo", cantidadhoras, "horas",  "y cobra sueldo de", sueldo)

#Bloque principal
calcular_sueldo("Ana", 10, 100)
calcular_sueldo(cantidadhoras=50, nombre="Juan", costohora=45)
