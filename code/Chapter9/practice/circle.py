import math
from shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = radius
    
    def area(self):
        return math.pi * self.__radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return "Circle: radius=%.2f, area=%.2f, perimeter=%.2f" % (
            self.__radius, self.area(), self.perimeter()
        )