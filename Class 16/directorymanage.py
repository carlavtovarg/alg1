import os
print(os.getcwd())
os.chdir("..\\Class15")
print((os.getcwd()))
os.chdir("..\\Class 16")
print(os.getcwd())
mylist = os.listdir()
for x in mylist:
    print(x)