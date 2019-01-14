import os
import sys
def file_exist(fName):
    if os.path.exists(fName):
      return True
    else:
        return False


fName = input("Enter the file name")
if file_exist(fName):
    with open(fName, 'r+') as f:
        try:
            print(f.read())
        except:
            print("There a problem with the file")
            sys.exit()
else:
    print("Could not read file:", fName)


