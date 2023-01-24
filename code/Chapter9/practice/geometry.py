from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from illegal_triangle_expception import IllegalTriangleException

def main():
    try:
        shapes = [
            Rectangle(10, 5),
            Circle(3),
            Triangle(3, 4, 5),
        ]

        for shape in shapes:
            print(shape)
    except ValueError as e:
        print(e)
    except IllegalTriangleException as e:
        print(e)

if __name__ == "__main__":
    main()