def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(year, month):
    days = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    elif month == 2:
        days = 29 if is_leap(year) else 28
    return days

def day_of_year(year, month, day):
    days = 0
    for i in range(1, month):
        days += days_in_month(year, i)
    days += day
    return days

def main():
    year, month, day = eval(input("Enter year, month, day: "))
    print(day_of_year(year, month, day))

if __name__ == "__main__":
    main()