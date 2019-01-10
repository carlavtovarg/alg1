import os
mylist = os.listdir()
for x in mylist:
    if os.path.isdir(x):
        print("FOLDER: ",end="")
    else:
        print("FILE: ", end="")
    print(x)

