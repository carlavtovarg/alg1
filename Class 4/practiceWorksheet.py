ex= input("Enter the exercise you want to try >>")
ex=int(ex)
if ex==1:
    age1 = input("Enter the fist age>>")
    age2 = input("Enter the second age>>")
    sum = int(age1) + int(age2)
    print("The sum of de ages is {0}".format(sum))
elif ex==2:
    college = input("Enter the name of the college>>")
    print("I am taking this course at "+college.title())
elif ex==3:
    price1 = input("Enter the fist price>>")
    price2 = input("Enter the second price>>")
    import decimal
    sum1 = decimal.Decimal(price1) + decimal.Decimal(price2)
    #sum1 = round(sum1, 2)
    print("The total sale price is {0}".format(sum1))
elif ex==4:
    price1 = input("Enter the total>>")
    price2 = input("Enter the increase rate>>")
    import decimal
    #price1 = float(price1)
    #price2 = float(price2)
    price1 = decimal.Decimal(price1)
    price2 = decimal.Decimal(price2)
   # percent = (float(price1)*float(price2))/100
    percent = price1 * price2 / 100
    total = price1 + percent
    print("The total amount increase by the percentage rate is: {0}".format(total))
elif ex==5:
    msj1 = input("Enter the fist msj>>")
    msj2 = input("Enter the second msj>>")
    msj3= msj1 + msj2
    print("the lenght of both of the variables var1 and var2 is ",len(msj3))
elif ex==6:
    for x in range(1, 11):
        print(x**2)
elif ex==7:
    for x in range(2):
        for y in range(2):
            for z in range(2):
                msj=str(x)+str(y)+str(z)
                print(msj)