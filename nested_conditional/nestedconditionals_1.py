grade_one = int(input("Ingresa la primera calificación: "))
grade_two = int(input("Ingresa la segunda calificación: "))
grade_three = int(input("Ingresa la tercera calificación: "))

average = (grade_one + grade_two + grade_three) / 3

if average >= 7:
    print("Aprobado")
else:
    if average >= 4:
        print("Regular")
    else:
        print("Reprobado")

