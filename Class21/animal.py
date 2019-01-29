class Animal:
    name = ""

class Fish(Animal):
    fish_species = ""

f = Fish()
f.name = "abc"

print(f.name)