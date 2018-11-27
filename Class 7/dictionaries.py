var=input("Insert the province code:")
var = var.upper()
#print(var)
provinces={'QU':'Quebec', 'NB':'New Brunswick','ON':'Ontario'}
try:
    print("The province is: " + provinces[var])
except KeyError:
    print("Key not exist")

for k,x in provinces.items():
    print(k,x)