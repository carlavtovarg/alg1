class Animal:
    name = ""
    species = ""

class Fish(Animal):
    def move(self):
        print("I am a fish and I swam.")
class Cat(Animal):
    def move(self):
        print("I am a Cat and I move if I smell food.")
c = Cat()
c.move()