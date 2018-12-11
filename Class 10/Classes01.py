class Cat:
        name = ""
        age = 0
        registered = False
        #constructor
        def __init__(self, input_name, input_age):
            self.name = input_name
            self.age = input_age

            if input_age > 2:
                self.registered = True
       #action object can do:
        def meow(self, number_times):
            for m in range(number_times):
                print("Meow")
#intantiation:
c1 = Cat("Tita", 7)
c2 = Cat("Gala", 6)

print("Cat c1 registration state is" + str(c1.registered))
print("Cat c2 registration state is" + str(c2.registered))
c1.meow(7)
del c1
del c2
