import os
def create_dir(dir):
    if os.path.exists(dir):
        print("The directory already exist")
        print(os.listdir(dir))
    else:
        os.mkdir(dir)
        print("The directory has be created")


print(os.getcwd())

directory = input("Enter the directory")
create_dir(directory)

