
#b="88"
#c= int(b)*2
#c= str(c)
#resul = "the number " + b + " doubled is " + c
#print (resul)
#print('the number {0} doubles is {1}'. format (b, c))
#print("*", end="")
#print("*", end="")
x = input("Enter a number >")
y = input("Enter a number2 >")
try:
    result = (int(x)/int(y))
except ZeroDivisionError:
    print("Sorry you cannot divide by zero")
except ValueError:
    print("Please enter just number")
except Exception:
    print("An unknown error has ocurred")
else:
    print(result)

