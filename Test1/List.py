my_list = []
new_element=""
def pr_list(list):
    cont = 1
    for x in my_list:
        print("{0}: {1}".format(cont, x))
        cont += 1

new_element = input("Please enter an element to add to the list[fin = finished]:")
while new_element!="fin":
    my_list.append(new_element)
    new_element = input("Please enter an element to add to the list[fin = finished]:")
if(len(my_list)>0):
    print("The list contains {0} elements, here they are:".format(len(my_list)))
    pr_list(my_list)
else:
    print("The list contains 0 elements")
