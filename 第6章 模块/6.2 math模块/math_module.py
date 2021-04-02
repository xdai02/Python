import math

def main():
    print("累加：%d" % math.fsum(range(101)))
    print("阶乘：%d" % math.factorial(10))
    print("乘方：%d" % math.pow(2, 10))
    print("对数：%f" % math.log(10))
    print("余数：%d" % math.fmod(22, 5))

if __name__ == "__main__":
    main()