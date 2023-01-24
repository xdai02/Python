from shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        if length < 0:
            raise ValueError("Length cannot be negative.")
        self.__length = length
    
    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width < 0:
            raise ValueError("Width cannot be negative.")
        self.__width = width
    
    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def __str__(self):
        return "Rectangle: length=%.2f, width=%.2f, area=%.2f, perimeter=%.2f" % (
            self.__length, self.__width, self.area(), self.perimeter()
        )