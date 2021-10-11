import re

def main():
    # 匹配成功返回Match类对象
    print("从头匹配：%s" % re.match("Hello", "Hello World"))
    print("不匹配：%s" % re.match("World", "Hello World"))
    # re.I / re.IGNORECASE表示忽略大小写比较
    print("忽略大小写：%s" % re.match("HELLO", "Hello World", re.I))

if __name__ == "__main__":
    main()