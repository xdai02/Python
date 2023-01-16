def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

def main():
    print(multiply(1, 2, 3))
    print(multiply(4, 2, 6, 1, 2))

if __name__ == "__main__":
    main()