import os
fName = input("enter the directory name>>")
if os.path.isdir(fName):
    print("The directory exist")
else:
    os.mkdir(fName)
    print("the directory has been created")