import re

def main():
    print("任意位置匹配：%s" % re.search(
            "python", "https://www.python.org/"))
    print("忽略大小写：%s" % re.search(
            "PYTHON", "https://www.python.org/", re.I))

if __name__ == "__main__":
    main()