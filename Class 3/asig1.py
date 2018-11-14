text1= "Fizz"
text2= "Buzz"
for x in range(0, 26):
    print("{0}:".format(x), end="")
    by3 = x % 3
    by5 = x % 5
    msj = ""
    if by3 == 0 and by5 == 0:
        msj= text1+text2
    elif by3 == 0 and by5 != 0:
        msj= text1
    elif by3 != 0 and by5 == 0:
        msj= text2
    print(msj)
