def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print("gcd(%d, %d) = %d" % (num1, num2, gcd(num1, num2)))

if __name__ == "__main__":
    main()