import csv
import random

HEADER = ["Location", "Longitude", "Latitude"]

def main():
    # 如果不使用newline，那么每行记录之间就会多出一个空行
    with open(file="location.csv", mode="w", 
              newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)       # 创建csv写入对象
        csv_writer.writerow(HEADER)         # 写入头部信息
        for i in range(1, 11):
            longitude = round(random.random() * 180, 3)   # [0, 180)
            latitude = round(random.random() * 90, 3)     # [0, 90)
            csv_writer.writerow(["loc-%d" % i, longitude, latitude])

if __name__ == "__main__":
    main()