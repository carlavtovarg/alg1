def calculate_tax(value):
    value_Plus= int(value)* 1.1234
    return value_Plus


value = input("enter a value")
print("the value is "+ str(calculate_tax(value)))