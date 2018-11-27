my_list1=[11, 22, 33, 44]
for item in my_list1:
    print(item)
    #---------------------------------------------------------

squares= [value**2 for value in range(1,11)]
print(squares)

#my_list= [str(value)+str(value) for value in range(1, 5)]
my_list= [value*11 for value in range(1, 5)]

my_list_3 = [2 ** n for n in range (0, 11)]
print(my_list_3)

inspeccion = [[True, True, False, True],
              [True, True, False, True],
              [True, True, False, True],
              [True, True, False, True]]
cont= 0
for value in inspeccion:
    cont+=1
    print("Inspection for car number {0}:".format(cont))
    print("inspector 1: {0}".format(value[0]))
    print("inspector 1: {0}".format(value[1]))
    print("inspector 1: {0}".format(value[2]))
    print("inspector 1: {0}".format(value[3]))



