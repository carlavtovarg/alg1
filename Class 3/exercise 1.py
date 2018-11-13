var1=input("Enter the age you started to work>>>>")
var2=input("Enter your current age>>>>")
try:
    var1 = int(var1)
    var2 = int(var2)
    var3 = var2 - var1
except ValueError:
    print("Please enter just number")
    flag= 1
except Exception:
    print("An unknown error has ocurred")
    flag = 1
else:
    if var3 < 0:
        print("Your current age cant be minus than the age you star working")
        flag = 1
    else:
        print("You have been working for {0} years".format(var3))
        flag = 0
while flag==1:
    var1 = input("Enter the age you started to work>>>>")
    var2 = input("Enter your current age>>>>")
    try:
        var1 = int(var1)
        var2 = int(var2)
        var3 = var2 - var1
    except ValueError:
        print("Please enter just number")
        flag == 1
    except Exception:
        print("An unknown error has ocurred")
        flag == 1
    else:
        print("You have been working for {0} years".format(var3))
        flag = 0
        break