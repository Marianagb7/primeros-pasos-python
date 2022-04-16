"""
Confeccionar una función que reciba una cadena de carácteres y nos devuelva los tres primeros.
En el bloque principal del programa definir una tupla con los nombres de meses.
Mostrar por pantalla los primeros tres carácteres de cada mes. 
"""
def primemeros_tres(cadena):
    return cadena[:3]

#Bloque principal
meses=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
"septiembre", "octubre", "noviembre", "diciembre")
for mes in meses:
    print(primemeros_tres(mes))
