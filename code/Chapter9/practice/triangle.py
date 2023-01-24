import math
from shape import Shape
from illegal_triangle_expception import IllegalTriangleException

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Sides cannot be negative.")
        
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise IllegalTriangleException("Cannot form a triangle.")

        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_sides(self):
        return (self.__side1, self.__side2, self.__side3)
    
    def set_sides(self, side1, side2, side3):
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Sides cannot be negative.")
        
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise IllegalTriangleException("Cannot form a triangle.")

        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def area(self):
        p = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3))
        
    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return "Triangle: sides=%s, area=%.2f, perimeter=%.2f" % (
            str(self.get_sides()), self.area(), self.perimeter()
        )