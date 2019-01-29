f = open("test_file.txt", 'w+')
f.write("Champlain VR")
f.seek(0)
print(f.read())