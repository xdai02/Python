from rectangle import Rectangle
from circle import Circle
from triangle import Triangle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(3),
        Triangle(3, 4, 5),
    ]

    for shape in shapes:
        print(shape)

if __name__ == "__main__":
    main()