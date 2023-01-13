year = int(input("Enter a year: "))

"""
    A year is a leap year if it is
    1. exactly divisible by 4, and not divisible by 100;
    2. or is exactly divisible by 400
"""
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Common year")