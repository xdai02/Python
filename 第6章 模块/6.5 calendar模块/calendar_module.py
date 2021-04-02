import calendar

def main():
    calendar.setfirstweekday(calendar.SUNDAY)
    print(calendar.month(2021, 4))

    print("2020是闰年吗？%s" % calendar.isleap(2020))
    print("2000-3000年间闰年数量：%d" % calendar.leapdays(2000, 3000))

    print(calendar.calendar(2021))


if __name__ == "__main__":
    main()