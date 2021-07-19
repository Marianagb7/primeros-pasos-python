accountant_one = 0
accountant_two = 0
outlay = 0
x = 1
n = int(input("Ingresa el número de trabajadores de la empresa: "))
while x <= n:
    salary = float(input("Ingresa el salario de cada trabajador: "))
    if salary <=300:
        accountant_one = accountant_one + 1
    else:
        accountant_two = accountant_two + 1
    outlay = outlay + salary
    x = x + 1
print("Total de trabajadores que devengan entre 100 y 300 dólares: ")
print(accountant_one)
print("Total de trabajadores que devengan más 300 dólares: ")
print(accountant_two)
print("Valor total nomina:  ")
print(outlay)



