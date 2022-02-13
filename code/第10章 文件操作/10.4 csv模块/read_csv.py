import csv

def main():
    with open(file="location.csv", mode="r", 
              newline="", encoding="utf-8") as file:
        csv_reader = csv.reader(file)   # 创建csv读取对象
        header = next(csv_reader)       # 读取标题行
        print(header)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    main()