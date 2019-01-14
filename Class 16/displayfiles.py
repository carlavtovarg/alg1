import os
ppal_dir = os.listdir()
#lista = []
exit = False


def print_lis(list, opc):
    count = 1
    for x in list:
        print(count, end="")
        print("  " + x)
        count += 1

my_list = os.listdir()
print_lis(my_list)
dir_number = (input("Enter the directory number you want to list the files>>"))
while exit == False:
    if int(dir_number):
        index = int(dir_number) - 1
    elif dir_number == "x":

    if os.path.isdir(my_list[index]):
        new_list = os.listdir(my_list[index])
        print_lis(new_list)
        print("Enter the directory number you want to list the files")
        print("Enter x if you want go back to principal directory ")
        dir_number = input("Enter .. if you want go back one directory >>")
    else:
        print("This is not a directory")



