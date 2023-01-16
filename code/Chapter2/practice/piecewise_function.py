x = float(input("Enter x: "))

if x < -2:
    y = 0.5 * x + 3
elif -2 <= x <= 2:
    y = 0
else:
    y = 4 ** x

print("y = %.2f" % y)