#Ingresar un email por teclado. Verificar si el string ingresado contiene solo u carácter @
email=input("Ingresa Un Email: ")
quantity=0
x=0
while x<len(email):
    if email[x]== "@":
        quantity=quantity+1
    x=x+1
if quantity==1:
    print("Contiene un solo caracter @ el email ingresado es correcto")
else:
    print("Incorrecto no es un email")
