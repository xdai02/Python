import math

side1, side2, side3 = eval(input("Enter three sides of a triangle: "))

if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Invalid")
else:
    p = (side1 + side2 + side3) / 2
    area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    print("Area = %.2f" % area)