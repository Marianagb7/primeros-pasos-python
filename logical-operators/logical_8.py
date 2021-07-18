salary = int(input("Ingresar sueldo del operario: "))
career = int(input("Años laborados en la empresa: "))

if salary<500 and career>=10:
    increase = salary * 0.20
    salary_pay = salary + increase
    print(salary_pay)
else:
    if salary<500:
        increase = salary * 0.05
        salary_pay = salary + increase
        print(salary_pay)
    else:
        print(salary)
        