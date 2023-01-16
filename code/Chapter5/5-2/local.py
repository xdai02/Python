def swap(a, b):
    a, b = b, a
    print("swap(): a = %d, b = %d" % (a, b))

def main():
    a, b = 1, 2

    print("Before: a = %d, b = %d" % (a, b))
    swap(a, b)
    print("After: a = %d, b = %d" % (a, b))

if __name__ == "__main__":
    main()