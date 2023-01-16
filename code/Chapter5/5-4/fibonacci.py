def fibonacci(n):
    if n == 1 or n == 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def main():
    n = 7
    print(fibonacci(n))

if __name__ == "__main__":
    main()