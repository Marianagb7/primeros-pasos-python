list=[]
for x in range(10):
    value=int(input("Ingrese valor: "))
    list.append(value)

print(list)

position=0
while position<len(list):
    if list[position] == 5:
        list.pop(position)
    else:
        position=position+1
print (list)