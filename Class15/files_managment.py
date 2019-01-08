with open("example.txt") as f:
    lines = f.readlines()
text_file_size = 0
   # my_text = f.read()

for line in lines:
    #to know how much bytes has the file
    text_file_size += len(line)
    #print(line.rstrip())
    print(line)
print("Total File size is:" + str(text_file_size))