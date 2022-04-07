"""
Construir una función que reciba un string como parámetro y en forma opcional un segundo string con un
caracter. La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro.
"""
def titulo_sudrayado(titulo, caracter="*"):
    print(titulo)
    print(caracter*len(titulo))
#Bloque principal
titulo_sudrayado("sistemas de administración")
titulo_sudrayado("Sistema de ventas", "x")