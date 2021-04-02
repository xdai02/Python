num = 123       # 全局变量

def foo():
    num = 321   # 局部变量
    print("foo(): %d" % num)    # 321

def bar():
    global num  # 调用全局变量
    num = 456
    print("bar(): %d" % num)    # 456

def main():
    foo()
    print(num)  # 123
    bar()
    print(num)  # 456

if __name__ == "__main__":
    main()