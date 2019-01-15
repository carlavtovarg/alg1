import os
ppal_dir = os.listdir()
#lista = []
exit = False


def print_lis(list):
    count = 1
    for x in list:
        print(count, end="")
        print("  " + x)
        count += 1
def print_msj():
    print("Enter the directory number you want to list the files")
    print("Enter x if you want go back to principal directory ")
    print("Enter .. if you want go back one directory")
    dir_num =input("Enter e for Exit>> ")
    return dir_num


my_list = os.listdir()
print_lis(my_list)
dir_number = input("Enter the directory number you want to list the files>>")
while exit == False:
    if dir_number.isdigit():

        """The option is to look the list of files inside one directory"""
        index = int(dir_number) - 1
        print("The Folder name:" + my_list[index])
        os.chdir(my_list[index])
        print("Current dir:"+os.curdir)
        if os.path.isdir(my_list[index]):
            my_list = os.listdir(my_list[index])
            print_lis(my_list)
            dir_number = print_msj()
        else:
            print("This is not a directory")
            quit()
    elif dir_number == "x":
        """the option is to see the principal directory"""
        print_lis(ppal_dir)
        dir_number = print_msj()
    elif dir_number == "..":
        """The option is go back one directory """
        #path = "..\\" + my_list[index]
       # print(path)
        path1 = os.chdir("..")
        my_list = os.listdir(path1)
        print_lis(my_list)
        dir_number = print_msj()
    elif dir_number == "e":
        quit()
    else:
        print("Please enter an option valid")




