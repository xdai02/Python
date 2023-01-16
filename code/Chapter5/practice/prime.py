import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter a number: "))
    if is_prime(n):
        print("%d is a prime number" % n)
    else:
        print("%d is not a prime number" % n)

if __name__ == "__main__":
    main()