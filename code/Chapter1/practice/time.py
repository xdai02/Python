total = int(input("Enter total seconds: "))

hour = total // 3600
min = total % 3600 // 60
sec = total % 60

print("%d second(s) = %d hour(s) %d minute(s) %d second(s)" % (total, hour, min, sec))