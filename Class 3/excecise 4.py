
a=input("please enter the first caracter for the loop")
b=input("please enter the second caracter for the loop")

# 1A

if(type(a) == int and type(b) == str):
    print(str(a)+b)
elif(type(a) == str and type(b) == str):
    print(a + b)
elif(type(a) == str and type(b) == int):
    print(a + str(b))
else:
    print("concatenate both caracter:"+str(a) + str(b))
    sum=a+b
    print("adition both number"+str(sum))
