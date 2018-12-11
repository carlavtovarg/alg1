from math import pi
class Shape:
    colour: ""
class Circle(Shape):
    radius = 0
    def __init__(self, c, r):
        self.radius = r
        self.colour = c

    def get_area(self):
        return pi * (self.radius** 2)
class Rect(Shape):
    len = 0
    height = 0
    def __init__(self, c, h, l):
        self.height = h
        self.len = l
        self.colour = c
    def get_area(self):
        return self.len * self.height
shape = Rect("Red", 5, 10)
print(shape.get_area())