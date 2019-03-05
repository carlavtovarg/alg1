import re
import math

#Input_list = [12, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!"]
Input_list = [12, 5, 7, 26, 5]

def regex_is_numeric(caracter):
    if re.match("^[0-9]+$", caracter):
        return True
    else:
        return False

def regex_is_letter(caracter):
    if re.match("^[a-zA-Z]+$", caracter):
        return True
    else:
        return False

def regex_is_special_Caracter(caracter):
    if re.match("^[^A-Za-z0-9\s]+$", caracter):
        return True
    else:
        return False

def is_even(caracter):
    """I have to add the validation for number"""
    mod = caracter % 2
    if mod > 0:
        return False
    else:
        return True

def high_Value(my_list, caracter):
    maxvalue = caracter
    for y in my_list:
        if isinstance(y, int):
            if y > maxvalue:
                maxvalue = y
    if maxvalue == caracter:
        msj= "This is the highest number in the list"
    else:
        msj = "This is not the highest number in the list"
    return msj



for x in Input_list:
   print("Element #"x)
    if regex_is_numeric(str(x)):
        print(high_Value(Input_list, x))


