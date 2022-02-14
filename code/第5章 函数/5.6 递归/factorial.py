def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def main():
    print("40! = %d" % factorial(40))

if __name__ == "__main__":
    main()