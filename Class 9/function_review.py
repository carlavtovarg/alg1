def city_country(city, country="Unkwoun City"):
    print(city.title() +' is in ' + country.title())

#city_country("Santiago", "Chile")

def city_country2(city, country="Unkwoun City"):
    var_city= city.title() +',' + country.title()
    var_city = "{0}, {1}". format(city, country)
    return var_city

print(city_country2("Caracas", "Venezuela"))
print(city_country2("Caracas"))

def show_magicians(magicians):
    for x in magicians:
        print(x)

mag=["Harry", "Hermione", "Ron"]
show_magicians(mag)

def create_order(customer, *skus):
    print("The customer name is:"+ customer)
    for sku in skus:
        print(sku)

create_order("Carla", 1234234,990890,989048930)