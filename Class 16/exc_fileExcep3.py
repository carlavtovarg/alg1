import os
fName = input("Enter the file name")

try:
    f = open(fName, 'r+')

except IOError:
    print("Could not read file:", fName)
    sys.exit()

with f:
    reader = f.readlines()
    for row in reader:
        print(row.rstrip())
