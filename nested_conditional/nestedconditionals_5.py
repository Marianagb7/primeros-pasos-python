total_questions = int(input("Ingresa el número de preguntas realizadas: "))
total_correct = int(input("¿cuántas son correctas: "))

porcentaje = total_correct * 100 / total_questions

if porcentaje >= 90:
    print("Nivel máximo")
else:
    if porcentaje >= 75:
        print("nivel medio")
    else:
        if porcentaje >= 50:
            print("Regular")
        else:
            print("Fuera de nivel")
