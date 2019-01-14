import os
fName = input("Enter the file name")

if os.path.exists(fName):
    with open (fName, 'rb') as f:
        try:
           print(f.read())
        except:
            print("There a problem with the file")
            sys.exit()
else:
    print("Could not read file:", fName)

