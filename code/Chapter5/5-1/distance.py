import math

def square(x):
    return x ** 2

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt(square(x1 - x2) + square(y1 - y2))

x1, y1 = eval(input("Enter (x1, y1): "))
x2, y2 = eval(input("Enter (x2, y2): "))
print("Distance:", distance((x1, y1), (x2, y2)))