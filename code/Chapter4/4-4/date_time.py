date_time = "2023/1/14 23:26:51"

date, time = date_time.split(" ")

year, month, day = date.split("/")
hour, minute, second = time.split(":")

date = [day, month, year]
date = "/".join(date)

if int(hour) < 12:
    time = [hour, minute, second]
    time = ":".join(time) + " AM"
else:
    time = [str(int(hour) - 12), minute, second]
    time = ":".join(time) + " PM"

date_time = date + " " + time
print(date_time)