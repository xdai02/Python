import math

x1, y1 = eval(input("Enter point 1: "))
x2, y2 = eval(input("Enter point 2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance = %.2f" % distance)