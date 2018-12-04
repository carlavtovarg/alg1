def is_divisible(num,res):
    if num % res == 0:
        return True
    return False
text1= "Fizz"
text2= "Buzz"
for x in range(0, 26):
    print("{0} ".format(x), end="")
    msj = ""
    if is_divisible(x,3) and is_divisible(x,5):
        msj= text1+text2
    elif is_divisible(x,3) :
        msj= text1
    elif is_divisible(x,5):
        msj= text2
    print(msj)
