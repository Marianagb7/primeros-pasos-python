number = int(input("Ingresa un valor de 1 a 999: "))
if number < 10:
    print("Tiene un digito")
else:
    if number < 100:
        print("Tiene dos digitos")
    else:
        if number < 1000:
            print("Tiene tres digitos")
        else :
            print("Error al ingresar el valor")



    