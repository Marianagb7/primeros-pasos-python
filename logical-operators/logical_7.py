x = int(input("Ingresa la cordenada x: "))
y = int(input("Ingresa la cordenada y: "))

if x>0 and y>0:
    print("Se encuentre en el primer cuadrante")
else:
    if x<0 and y>0:
        print(" Se encuentra en el segundo cuadrante")
    else:
        if x<0 and y<0:
            print(" Se encuentra en el tercer cuadrante")
        else:
            if x>0 and y<0:
                print("Se encuentra en el cuarto cuadrante")
            else:
                print("Se encuentra sobre un eje")



