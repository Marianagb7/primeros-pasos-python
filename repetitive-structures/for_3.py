approved = 0
fails = 0

for i in range(10):
    grade = int(input("Ingresa las notas: "))
    if grade >= 7:
        approved = approved + 1
    else:
        fails = fails + 1
print("Total estudiantes aprobados: ", approved)
print("Total estudiantes reprobados: ", fails)


