filename = input('Enter a file name:')
try:
    with open(filename,'r') as f:
        print(f.read())
except IOError:
    print("there in no file named", filename)


