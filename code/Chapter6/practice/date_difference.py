import datetime

year, month, day = map(int, input("Enter the first date: ").split())
date1 = datetime.date(year, month, day)
year, month, day = map(int, input("Enter the second date: ").split())
date2 = datetime.date(year, month, day)

diff = date2 - date1
print("The difference between", date1, "and", date2, "is", diff.days, "days.")