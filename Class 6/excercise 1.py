import random
my_list = []
cont = 0
check = 0
while cont <= 10:
    check = 0
    valor = random.randint(1, 12)
    for a in my_list:
        if a == valor:
           check = 1
           break
    if check!=1:
        my_list.append(valor)
        cont+=1
print(my_list)