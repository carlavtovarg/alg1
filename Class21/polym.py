class Animal:

    def make_sound(self):
        print("I made a generic sound")


class Dog(Animal):

    def make_sound(self):
        print("Bark")

    def make_parent_sound(self):
        """this give access to make_sound from the parent"""
        super().make_sound()


d1 = Dog()
d1.make_sound()
d1.make_parent_sound()
