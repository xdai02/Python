def calculate(operator, *nums):
    """
        定义一个可变参数的数学计算
        通过传入的运算符和运算数进行计算
        Args:
            operator (str): 运算符
            nums (tuple): 运算数（可变参数）
        Return:
            计算结果
    """ 
    if operator == '+':
        result = 0
        for num in nums:
            result += num
    elif operator == '*':
        result = 1
        for num in nums:
            result *= num
    return result

def main():
    print("累加：%d" % calculate('+', 1, 2, 3, 4, 5))
    print("阶乘：%d" % calculate('*', 1, 2, 3, 4, 5))

if __name__ == "__main__":
    main()