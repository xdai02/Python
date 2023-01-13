from functools import reduce

def main():
    lst = list(range(10))

    filter_lst = list(filter(lambda x: x % 2 ==0, lst))
    print("过滤出偶数：%s" % filter_lst)

    map_lst = list(map(lambda x: x ** 2, filter_lst))
    print("平方：%s" % map_lst)

    result = reduce(lambda x, y: x+y, map_lst)
    print("求和：%d" % result)

if __name__ == "__main__":
    main()