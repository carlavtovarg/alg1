import random
my_list= []
suma=0
cont=0
check=0

for a in range(0,10):
    valor = random.randint(1, 100)
    my_list.append(valor)
    show_list=str(my_list[a])
    print("the value in the position {0} is: {1}".format(a, show_list))



#print("The array has {0} elements".format(len(my_list)))
#print("The max element is {0}".format(max(my_list)))
maxvalue= my_list[0]
for x in my_list:
    if x > maxvalue:
        maxvalue = x
minvalue = my_list[0]
for x in my_list:
    suma = suma + x
    cont+=1
    if x < minvalue:
        minvalue = x
print("The array has {0} elements".format(cont))
print("The max element is {0}".format(maxvalue))
print("The min element is {0}".format(minvalue))
print("The average is {0}".format(suma/cont))
#print("The max element is {0}".format(maxvalue))
#print("The min element is {0}".format(min(my_list)))
#print("The average is {0}".format(sum(my_list)/len(my_list)))