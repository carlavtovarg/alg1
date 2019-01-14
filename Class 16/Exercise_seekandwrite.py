with open ("testfile2.txt",'w+') as f:
    f.write("Testing 123")
    print(f.read())
    f.seek(4)
    f.write("*")
    f.seek(0)
    print(f.read())
    f.seek(0)
    f.write("C")
    f.seek(0)
    print(f.read())

