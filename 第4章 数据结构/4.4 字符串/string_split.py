ip = "127.0.0.1"
print("ip信息：%s" % ip.split("."))

date_time = "2021/03/31 17:32:53"
item = date_time.split(" ")
print("date信息：%s" % item[0].split("/"))
print("time信息：%s" % item[1].split(":"))